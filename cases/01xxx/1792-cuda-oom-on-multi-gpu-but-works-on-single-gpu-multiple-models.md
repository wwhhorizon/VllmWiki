# vllm-project/vllm#1792: CUDA OOM on Multi GPU but works on single GPU, multiple models

| 字段 | 值 |
| --- | --- |
| Issue | [#1792](https://github.com/vllm-project/vllm/issues/1792) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA OOM on Multi GPU but works on single GPU, multiple models

### Issue 正文摘录

I attempted to run a number of models through two GPU and got OOM however this was successful with single GPU. Initially I thought my model was too large when running a 34B version and scaled down to 6.7B however it did not work with 6.7B either. But testing the 6.7B with single GPU worked so I am assuming this is an issue with the distributed compute with multiple GPU rather than an actual memory constraint. Models tested: TheBloke/deepseek-coder-6.7B-instruct-AWQ TheBloke/deepseek-coder-33B-instruct-AWQ TheBloke/Phind-CodeLlama-34B-v2-AWQ python -m vllm.entrypoints.openai.api_server --model TheBloke/deepseek-coder-6.7B-instruct-AWQ --served-model-name gpt-3.5-turbo-16k-0613 --tensor-parallel-size 2 --max-model-len 16384 --quantization awq --dtype half --load-format safetensors --tokenizer-mode auto --trust-remote-code & npx localtunnel --port 8000 [6] 11724 your url is: https://heavy-bags-hide.loca.lt INFO 11-26 14:01:26 api_server.py:638] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name='gpt-3.5-turbo-16k-0613', model='TheBloke/deepseek-coder-6.7B-instruct-AWQ', tokenizer=None,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: nitially I thought my model was too large when running a 34B version and scaled down to 6.7B however it did not work with 6.7B either. But testing the 6.7B with single GPU worked so I am assuming this is an issue with t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: CUDA OOM on Multi GPU but works on single GPU, multiple models I attempted to run a number of models through two GPU and got OOM however this was successful with single GPU. Initially I thought my model was too large wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ingle GPU. Initially I thought my model was too large when running a 34B version and scaled down to 6.7B however it did not work with 6.7B either. But testing the 6.7B with single GPU worked so I am assuming this is an...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:638] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name='gpt-3.5-turbo-16k-0613', model='TheBloke/deepseek-cod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: CUDA OOM on Multi GPU but works on single GPU, multiple models I attempted to run a number of models through two GPU and got OOM however this was successful with single GPU. Initially I thought my model was too large whe

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
