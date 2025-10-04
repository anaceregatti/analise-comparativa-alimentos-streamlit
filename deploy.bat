@echo off
echo ========================================
echo   DEPLOY STREAMLIT CLOUD - v1.0 Stable
echo ========================================
echo.

echo 1. Verificando status do Git...
git status
echo.

echo 2. Fazendo push para GitHub...
git push -u origin main
echo.

echo 3. Verificando remote...
git remote -v
echo.

echo 4. Deploy concluido!
echo.
echo ========================================
echo   PROXIMOS PASSOS:
echo ========================================
echo 1. Acesse: https://share.streamlit.io
echo 2. Clique em "New app"
echo 3. Repository: SecretariaAnaCeregatti/analise-comparativa-alimentos-streamlit
echo 4. Branch: main
echo 5. Main file path: app.py
echo 6. Python version: 3.11
echo 7. Clique em "Deploy!"
echo.
echo URL esperada: https://analise-comparativa-alimentos-streamlit.streamlit.app
echo ========================================
pause
