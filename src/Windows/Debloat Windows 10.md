# Debloating Windows 10


## Removing packages with Powershell


### Remove YourPhone

```Powershell
Get-AppxPackage *Microsoft.YourPhone* -AllUsers | Remove-AppxPackage
```