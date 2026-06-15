# vllm-project/vllm#3448: [Bug]: Bug in Guided Generation Logits Processorwith `n>1`

| 字段 | 值 |
| --- | --- |
| Issue | [#3448](https://github.com/vllm-project/vllm/issues/3448) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bug in Guided Generation Logits Processorwith `n>1`

### Issue 正文摘录

### Your current environment I used Docker: ``` git clone https://github.com/vllm-project/vllm.git git pull origin pull/3211/head docker build --target test -t vllm-grammars . docker run --gpus=all -it vllm-grammars ``` On the server with 4x NVIDIA RTX A4000 ### 🐛 Describe the bug I tested the `Context Free Grammar` with vLLM and asked `phi-1` to generate a simple SQL query, following this [test](https://github.com/simon-mo/vllm/blob/7290ea75f9bdee72c2d4c18e5fd27d2d5d464e4e/tests/entrypoints/test_openai_server.py#L679) from a recent [PR](https://github.com/vllm-project/vllm/pull/3211) ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.model_executor.guided_logits_processors import CFGLogitsProcessor model = "microsoft/phi_1" prompt = "Writa a simple SQL query to the table table_2 checking if col_1 equals to 1" tokenizer = AutoTokenizer.from_pretrained(model) simple_sql_grammar = """ start: select_statement select_statement: "SELECT" column "from" table "where" condition column: "col_1" | "col_2" table: "table_1" | "table_2" condition: column "=" number number: "1" | "2" """ sampling_params = SamplingParams( temperature=0.7, top_p=0.95, n=10,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ogits Processorwith `n>1` bug;stale ### Your current environment I used Docker: ``` git clone https://github.com/vllm-project/vllm.git git pull origin pull/3211/head docker build --target test -t vllm-grammars . docker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: docker run --gpus=all -it vllm-grammars ``` On the server with 4x NVIDIA RTX A4000 ### 🐛 Describe the bug I tested the `Context Free Grammar` with vLLM and asked `phi-1` to generate a simple SQL query, following this [t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: LogitsProcessor(simple_sql_grammar, tokenizer)] ) llm = LLM(model=model, dtype="auto") outputs = llm.generate([prompt], sampling_params) print([ output_.text for output_ in outputs[0].outputs ]) ``` Although the `CFGLog...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.model_executor.guided_logits_processors import CFGLogitsProcessor model = "microsoft/phi_1" prompt = "Writa a simple SQL query to the table table_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: n;sampling_logits attention;cuda;quantization;sampling build_error;crash;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
