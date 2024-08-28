CREATE TABLE "tb_cotacao" (
  "co_cotacao" integer PRIMARY KEY,
  "vl_cotacao" float,
  "dt_cotacao" date,
  "created_at" timestamp not null default now()
);

CREATE TABLE "tb_consulta" (
  "co_consulta" serial PRIMARY KEY,
  "dt_inicio_consulta" date,
  "dt_fim_consulta" date,
  "created_at" timestamp not null default now()
);

CREATE TABLE "tb_execucao" (
  "co_execucao" serial PRIMARY KEY,
  "co_consulta" integer,
  "nu_execucoes" integer,
  "nu_dias" integer,
  "vl_cotacao_alvo" float,
  "vl_probabilidade" float,
  "vl_intervalo_confianca_inferior" float,
  "vl_intervalo_confianca_superior" float,
  "created_at" timestamp not null default now()
);

ALTER TABLE "tb_execucao" ADD FOREIGN KEY ("co_consulta") REFERENCES "tb_consulta" ("co_consulta");


