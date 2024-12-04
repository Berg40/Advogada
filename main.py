import os
import flet as ft


def main(page: ft.Page):
    page.title = "Cálculo de Rescisão Contratual"
    page.scroll = "auto"

    # Inputs para dados do cálculo
    salario_mensal = ft.TextField(label="Salário mensal do empregado (R$)", keyboard_type="number", width=300)
    meses_trabalhados = ft.TextField(label="Meses trabalhados no ano atual", keyboard_type="number", width=300)
    saldo_fgts = ft.TextField(label="Saldo do FGTS (R$)", keyboard_type="number", width=300)
    dias_aviso_previo = ft.TextField(label="Dias de aviso prévio (mínimo 30)", keyboard_type="number", width=300)
    dias_ferias_vencidas = ft.TextField(label="Dias de férias vencidas (0 se não houver)", keyboard_type="number",
                                        width=300)
    horas_extras = ft.TextField(label="Total de horas extras feitas", keyboard_type="number", width=300)
    valor_hora_extra = ft.TextField(label="Valor da hora extra (R$)", keyboard_type="number", width=300)
    adicional_noturno = ft.TextField(label="Adicional noturno (R$)", keyboard_type="number", width=300)
    insalubridade = ft.TextField(label="Insalubridade (R$)", keyboard_type="number", width=300)
    periculosidade = ft.TextField(label="Periculosidade (R$)", keyboard_type="number", width=300)

    resultado = ft.Text("", size=16)

    # Função para calcular a rescisão
    def calcular_rescisao(e):
        try:
            # Conversão dos valores para float ou int
            salario = float(salario_mensal.value)
            meses = int(meses_trabalhados.value)
            fgts = float(saldo_fgts.value)
            aviso = int(dias_aviso_previo.value)
            ferias_vencidas = int(dias_ferias_vencidas.value)
            horas = float(horas_extras.value)
            valor_hora = float(valor_hora_extra.value)
            adicional_n = float(adicional_noturno.value)
            insal = float(insalubridade.value)
            peril = float(periculosidade.value)

            # Cálculos
            aviso_previo = (salario / 30) * aviso
            multa_fgts = fgts * 0.4
            valor_ferias_vencidas = (salario / 30) * ferias_vencidas
            ferias_proporcionais = (salario / 12) * (meses / 12)
            decimo_terceiro = (salario / 12) * meses
            total_horas = horas * valor_hora
            adicionais = adicional_n + insal + peril

            total = (aviso_previo + multa_fgts + valor_ferias_vencidas +
                     ferias_proporcionais + decimo_terceiro +
                     total_horas + adicionais)

            # Atualizar resultado
            resultado.value = (
                f"Aviso prévio: R$ {aviso_previo:.2f}\n"
                f"Multa FGTS (40%): R$ {multa_fgts:.2f}\n"
                f"Férias vencidas: R$ {valor_ferias_vencidas:.2f}\n"
                f"Férias proporcionais: R$ {ferias_proporcionais:.2f}\n"
                f"13º proporcional: R$ {decimo_terceiro:.2f}\n"
                f"Horas extras: R$ {total_horas:.2f}\n"
                f"Adicionais: R$ {adicionais:.2f}\n"
                f"\nTotal: R$ {total:.2f}"
            )
            page.update()
        except Exception as ex:
            resultado.value = f"Erro no cálculo: {str(ex)}"
            page.update()

    # Botão para realizar o cálculo
    calcular_button = ft.ElevatedButton("Calcular Rescisão", on_click=calcular_rescisao)

    # Adicionando os elementos à página
    page.add(
        ft.Text("Cálculo de Rescisão Contratual", size=20, weight="bold"),
        salario_mensal,
        meses_trabalhados,
        saldo_fgts,
        dias_aviso_previo,
        dias_ferias_vencidas,
        horas_extras,
        valor_hora_extra,
        adicional_noturno,
        insalubridade,
        periculosidade,
        calcular_button,
        resultado
    )


# Configurar porta para o Render
port = int(os.environ.get("PORT", 8080))
ft.app(target=main, port=port, view=ft.WEB_BROWSER)
