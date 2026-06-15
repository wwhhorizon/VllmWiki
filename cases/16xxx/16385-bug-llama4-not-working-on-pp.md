# vllm-project/vllm#16385: [Bug]: LLama4 Not working on PP

| 字段 | 值 |
| --- | --- |
| Issue | [#16385](https://github.com/vllm-project/vllm/issues/16385) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLama4 Not working on PP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running into an issue where i am unable to launch Llama-4-Maverick-17B-128E-Instruct-FP8 in a distributed fashion using Ray. As you can see below, VLLM is able to successfully connect to the Ray cluster, however it looks like the value for `architectures` appears to be None on the way workers node. Looking through the stack trace i can see that `architectures` is being set to `None` despite both the `config.json` and the `--hf-overides` flag both specifying `{"architectures": ["Llama4ForConditionalGeneration"]}` I can confirm this is only happening for llama4 and was able to successfully distribute 3.3 over 16 X A 100. ``` VLLM_DISABLE_COMPILE_CACHE=1 python -m vllm.entrypoints.openai.api_server --model /home/jovyan/llama4-llm-vol/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --served-model-name Llama-4-Maverick-17B-128E-Instruct-FP8 --enforce-eager --max-model-len 2000 --tensor-parallel 8 --pipeline-parallel-size 2 --gpu-memory-utilization 0.95 --host 0.0.0.0 --distributed-executor-backend ray --port 8000 --quantization compressed-tensors --hf-overrides '{"architectures": ["Llama4ForConditionalGeneration"]}' INFO 04-10...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: one` despite both the `config.json` and the `--hf-overides` flag both specifying `{"architectures": ["Llama4ForConditionalGeneration"]}` I can confirm this is only happening for llama4 and was able to successfully distr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: an issue where i am unable to launch Llama-4-Maverick-17B-128E-Instruct-FP8 in a distributed fashion using Ray. As you can see below, VLLM is able to successfully connect to the Ray cluster, however it looks like the va...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ssfully connect to the Ray cluster, however it looks like the value for `architectures` appears to be None on the way workers node. Looking through the stack trace i can see that `architectures` is being set to `None` d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/home/jovyan/llama4-llm-vol/meta-lla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: LLama4 Not working on PP bug ### Your current environment ### 🐛 Describe the bug I am running into an issue where i am unable to launch Llama-4-Maverick-17B-128E-Instruct-FP8 in a distributed fashion using Ray. As

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
