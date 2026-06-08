@echo off
REM Script para remover metadados de arquivos DOCX usando PowerShell
REM Funciona com Microsoft Word ou LibreOffice

echo.
echo ════════════════════════════════════════════════════════════════════════
echo           REMOVER METADADOS - SUBMISSÃO CGU
echo ════════════════════════════════════════════════════════════════════════
echo.
echo Este script vai remover metadados dos 3 arquivos DOCX necessários:
echo   1. artigo_igro_final.docx
echo   2. capa_anonimizada.docx
echo   3. informacoes_autoria.docx
echo.
echo ════════════════════════════════════════════════════════════════════════
echo.

REM Método 1: Usando PowerShell (se disponível)
echo [INFO] Tentando usar PowerShell...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$files = @('artigo_igro_final.docx', 'capa_anonimizada.docx', 'informacoes_autoria.docx'); ^
   foreach($file in $files) { ^
     if(Test-Path $file) { ^
       echo \"Processando: $file...\"; ^
       $com = New-Object -ComObject Word.Application; ^
       $doc = $com.Documents.Open((Resolve-Path $file).Path); ^
       $doc.Save(); ^
       $com.Quit(); ^
       echo \"✓ $file processado\"; ^
     } ^
   }" 2>nul

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ════════════════════════════════════════════════════════════════════════
    echo ✓ SUCESSO! Metadados removidos de todos os 3 arquivos.
    echo ════════════════════════════════════════════════════════════════════════
    echo.
) else (
    echo.
    echo ════════════════════════════════════════════════════════════════════════
    echo ⚠ Método automático não funcionou. Use o método manual:
    echo ════════════════════════════════════════════════════════════════════════
    echo.
    echo MÉTODO MANUAL (Microsoft Word):
    echo.
    echo Para CADA arquivo (artigo_igro_final.docx, capa_anonimizada.docx, informacoes_autoria.docx):
    echo.
    echo   1. Abra o arquivo em Microsoft Word
    echo   2. Clique em: File ^> Info
    echo   3. Clique em: "Inspect Document"
    echo   4. Marque TODAS as opções:
    echo      ☑ Document Properties and Personal Information
    echo      ☑ Comments and Annotations
    echo      ☑ Custom XML Data
    echo      ☑ Headers and Footers
    echo      ☑ Hidden Text
    echo      ☑ All Fields
    echo   5. Clique em: "Remove All"
    echo   6. Clique em: "Close"
    echo   7. Salve o arquivo (Ctrl+S)
    echo   8. Verifique em File ^> Info se não há mais autor/título/sujeito
    echo.
    echo Ou use ferramenta online: https://cloudconvert.com/ ^(opção: remove metadata^)
    echo.
)

pause
