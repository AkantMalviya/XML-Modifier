$endpoint  = "http://CMTL-DBV1PAY01:2525/HCM_Payroll/api/BasicInformation/GetInformation"
$requestData = @{
    ClientCode = "ABC"
    Language = "1033"
    Identifiers = "ArielDB-Member:999999,ArielPayroll:00000000000,RequestCode:CAS-1234-XYZ"
}
$result = Invoke-RestMethod -UseBasicParsing -Uri $endpoint -Method Post -Body $requestData
#Show the Data
$result.data