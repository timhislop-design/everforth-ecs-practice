# Cowork Linux Environment — Fix & Reinstall Guide

**Symptom:** Cowork shell/sandbox fails with:
`HCS operation failed: failed to start VM: HcsWaitForOperationResult failed with HRESULT 0x80070005: Access is denied.`

**What it means:** `0x80070005` = *Access Denied* from the Windows Host Compute Service (HCS). The Cowork VM service (`CoworkVMService`) runs as `LocalSystem`, but on Microsoft Store (MSIX) installs the VM bundle folder often has **no ACL entry for `NT AUTHORITY\SYSTEM`**, so HCS can't attach the VM's virtual disks. This is a documented Cowork-on-Windows bug (anthropics/claude-code #38188).

**The confirmed fix:** grant `SYSTEM` (and your user) Full Control on the `vm_bundles` folder, then restart the HCS + Cowork services.

---

## Fix — do this first (resolves 0x80070005)

1. **Fully quit Claude Desktop.** Right-click the tray icon → **Quit** (don't just close the window).

2. **Open PowerShell as Administrator.** Start → type *PowerShell* → right-click → **Run as administrator**.

3. **Grant SYSTEM + your user Full Control on the VM bundle folder.** Paste this whole block — it auto-locates the folder for both MSIX and standard installs:

   ```powershell
   $pkg = (Get-AppxPackage *Claude*).PackageFamilyName
   $paths = @(
     "$env:LOCALAPPDATA\Packages\$pkg\LocalCache\Roaming\Claude\vm_bundles",
     "$env:APPDATA\Claude\vm_bundles"
   ) | Where-Object { $_ -and (Test-Path $_) }

   foreach ($p in $paths) {
     Write-Host "Fixing ACLs on $p"
     icacls $p /grant "SYSTEM:(OI)(CI)F" /T
     icacls $p /grant "$env:USERNAME:(OI)(CI)F" /T
   }
   ```

4. **Restart the HCS + Cowork services:**

   ```powershell
   net stop CoworkVMService
   net stop vmcompute
   net start vmcompute
   net start CoworkVMService
   ```

5. **Relaunch Claude Desktop** and start a Cowork session. Test with a shell command (e.g. `python3 --version`).

---

## If it still fails

**A. Disable the Windows "Containers" feature** (a separate cause of HCS `0x800701c0` / `0x80070005`, needs a reboot):

```powershell
Disable-WindowsOptionalFeature -Online -FeatureName Containers -NoRestart
```
Then **reboot** and retry the session.

**B. Verify the required Windows features are on** (elevated PowerShell):

```powershell
Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform, Microsoft-Hyper-V-All | Select FeatureName, State
```
Both should be **Enabled**. If not:
```powershell
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -All
```
Reboot after enabling. (Note: full Hyper-V requires Windows 11 **Pro/Enterprise** — Home edition can't run the Cowork VM.)

**C. Confirm virtualization is enabled in BIOS/UEFI** (Intel VT-x / AMD-V). Task Manager → Performance → CPU → "Virtualization: Enabled".

---

## Force a clean reinstall of the workspace VM

If the bundle itself is corrupt, force Claude to re-download it (~9 GB):

1. Fully quit Claude Desktop.
2. In elevated PowerShell, rename the bundle so Claude rebuilds it:
   ```powershell
   $pkg = (Get-AppxPackage *Claude*).PackageFamilyName
   $vm = "$env:LOCALAPPDATA\Packages\$pkg\LocalCache\Roaming\Claude\vm_bundles"
   if (-not (Test-Path $vm)) { $vm = "$env:APPDATA\Claude\vm_bundles" }
   Rename-Item $vm "vm_bundles_old_$(Get-Date -Format yyyyMMdd)"
   ```
3. Also clear the one-shot reinstall guard if present:
   ```powershell
   Get-ChildItem "$env:APPDATA\Claude" -Recurse -Filter ".auto_reinstall_attempted" -ErrorAction SilentlyContinue | Remove-Item -Force
   ```
4. Relaunch Claude Desktop — it re-downloads the VM bundle on first Cowork session.
5. **Re-run the SYSTEM ACL grant (Fix step 3 above)** on the newly created `vm_bundles` folder, since a fresh download can recreate the folder without the SYSTEM entry.

---

## Notes
- The ACL grant (Fix step 3) is the specific action that resolved the `0x80070005` error in the tracked bug.
- A small number of users hit a secondary issue where the VM boots but Claude Desktop times out connecting to it (linked to Windows **Credential Guard**). If you see "VM service not running" *after* the ACL fix, that's the separate frontend-connect issue — restart Claude Desktop; if it persists, report on the tracking issue below.

**References:**
- anthropics/claude-code #38188 — HCS 0x80070005, SYSTEM ACL missing (root cause + fix)
- anthropics/claude-code #37068 — HCS Construct failure w/ Containers feature enabled
- anthropics/claude-code #32574 — main Windows Cowork virtualization tracking issue
