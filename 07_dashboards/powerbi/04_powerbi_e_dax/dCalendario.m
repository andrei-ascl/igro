let
    DataInicial = #date(2023, 1, 1),
    DataFinal = #date(2027, 12, 31),
    Hoje = Date.From(DateTime.LocalNow()),

    ListaDatas = List.Dates(
        DataInicial,
        Duration.Days(DataFinal - DataInicial) + 1,
        #duration(1, 0, 0, 0)
    ),

    Fonte = Table.FromList(ListaDatas, Splitter.SplitByNothing(), {"Date"}),
    TipoData = Table.TransformColumnTypes(Fonte, {{"Date", type date}}),

    AddAno = Table.AddColumn(TipoData, "Ano", each Date.Year([Date]), Int64.Type),
    AddMes = Table.AddColumn(AddAno, "Mes", each Date.Month([Date]), Int64.Type),
    AddDia = Table.AddColumn(AddMes, "Dia", each Date.Day([Date]), Int64.Type),
    AddNomeMes = Table.AddColumn(AddDia, "NomeMes", each Text.Proper(Date.MonthName([Date], "pt-BR")), type text),
    AddMesAbrev = Table.AddColumn(
        AddNomeMes,
        "MesAbrev",
        each {"jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"}{[Mes] - 1},
        type text
    ),
    AddAnoMes = Table.AddColumn(AddMesAbrev, "AnoMes", each [Ano] * 100 + [Mes], Int64.Type),

    AddNumDiaSemana = Table.AddColumn(AddAnoMes, "NumDiaSemana", each Date.DayOfWeek([Date], Day.Monday) + 1, Int64.Type),
    AddNomeDiaSemana = Table.AddColumn(AddNumDiaSemana, "NomeDiaSemana", each Text.Proper(Date.DayOfWeekName([Date], "pt-BR")), type text),
    AddDiaSemanaAbrev = Table.AddColumn(
        AddNomeDiaSemana,
        "DiaSemanaAbrev",
        each {"Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"}{[NumDiaSemana] - 1},
        type text
    ),
    AddNumSemanaAno = Table.AddColumn(AddDiaSemanaAbrev, "NumSemanaAno", each Date.WeekOfYear([Date], Day.Monday), Int64.Type),
    AddAnoSemana = Table.AddColumn(AddNumSemanaAno, "AnoSemana", each [Ano] * 100 + [NumSemanaAno], Int64.Type),

    AddTrimestre = Table.AddColumn(AddAnoSemana, "Trimestre", each Number.RoundUp([Mes] / 3), Int64.Type),
    AddQuadrimestre = Table.AddColumn(AddTrimestre, "Quadrimestre", each if [Mes] <= 4 then 1 else if [Mes] <= 8 then 2 else 3, Int64.Type),
    AddNomeQuadrimestre = Table.AddColumn(AddQuadrimestre, "NomeQuadrimestre", each Text.From([Quadrimestre]) & "º Quadrimestre", type text),
    AddAnoQuadri = Table.AddColumn(AddNomeQuadrimestre, "AnoQuadri", each [Ano] * 10 + [Quadrimestre], Int64.Type),
    AddSemestre = Table.AddColumn(AddAnoQuadri, "Semestre", each if [Mes] <= 6 then 1 else 2, Int64.Type),

    AddFimDeSemana = Table.AddColumn(AddSemestre, "FimDeSemana", each [NumDiaSemana] >= 6, type logical),
    AddDiaUtil = Table.AddColumn(AddFimDeSemana, "DiaUtil", each [NumDiaSemana] <= 5, type logical),
    AddPrimeiroDiaMes = Table.AddColumn(AddDiaUtil, "PrimeiroDiaMes", each [Dia] = 1, type logical),
    AddUltimoDiaMes = Table.AddColumn(AddPrimeiroDiaMes, "UltimoDiaMes", each [Date] = Date.EndOfMonth([Date]), type logical),
    AddAnoAtual = Table.AddColumn(AddUltimoDiaMes, "AnoAtual", each [Ano] = Date.Year(Hoje), type logical),
    AddUltimos12Meses = Table.AddColumn(AddAnoAtual, "Ultimos12Meses", each [Date] >= Date.AddMonths(Hoje, -12) and [Date] <= Hoje, type logical),
    AddUltimoQuadrimestre = Table.AddColumn(AddUltimos12Meses, "UltimoQuadrimestre", each [Date] >= Date.AddMonths(Hoje, -4) and [Date] <= Hoje, type logical),

    AddMesExercicio = Table.AddColumn(
        AddUltimoQuadrimestre,
        "MesExercicio",
        each if [Ano] >= 2024 then ([Ano] - 2024) * 12 + [Mes] else null,
        Int64.Type
    ),
    AddQuadriExercicio = Table.AddColumn(
        AddMesExercicio,
        "QuadriExercicio",
        each if [Ano] >= 2024 then ([Ano] - 2024) * 3 + [Quadrimestre] else null,
        Int64.Type
    ),
    AddDiaDoAno = Table.AddColumn(AddQuadriExercicio, "DiaDoAno", each Date.DayOfYear([Date]), Int64.Type),

    AddDiaUtilDoMes = Table.AddColumn(
        AddDiaDoAno,
        "DiaUtilDoMes",
        each
            let
                DataAtual = [Date],
                InicioMes = Date.StartOfMonth(DataAtual),
                DatasAteDia = List.Dates(InicioMes, Duration.Days(DataAtual - InicioMes) + 1, #duration(1, 0, 0, 0)),
                DiasUteis = List.Select(DatasAteDia, each Date.DayOfWeek(_, Day.Monday) < 5)
            in
                List.Count(DiasUteis),
        Int64.Type
    ),

    AddTrimestreLabel = Table.AddColumn(AddDiaUtilDoMes, "TrimestreLabel", each "T" & Text.From([Trimestre]) & "/" & Text.From([Ano]), type text),
    AddQuadriLabel = Table.AddColumn(AddTrimestreLabel, "QuadriLabel", each "Q" & Text.From([Quadrimestre]) & "/" & Text.From([Ano]), type text),
    AddSemestreLabel = Table.AddColumn(AddQuadriLabel, "SemestreLabel", each "S" & Text.From([Semestre]) & "/" & Text.From([Ano]), type text),
    AddAnoMesLabel = Table.AddColumn(AddSemestreLabel, "AnoMesLabel", each [MesAbrev] & "/" & Text.From([Ano]), type text)
in
    AddAnoMesLabel
