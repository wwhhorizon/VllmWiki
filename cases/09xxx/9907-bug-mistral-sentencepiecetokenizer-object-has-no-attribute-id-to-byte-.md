# vllm-project/vllm#9907: [Bug]:   Mistral 'SentencePieceTokenizer' object has no attribute 'id_to_byte_piece'

| 字段 | 值 |
| --- | --- |
| Issue | [#9907](https://github.com/vllm-project/vllm/issues/9907) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:   Mistral 'SentencePieceTokenizer' object has no attribute 'id_to_byte_piece'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug python code: ``` vllm serve mistralai/Mistral-Large-Instruct-2407 \ --tokenizer_mode mistral \ --config_format mistral \ --load_format mistral ``` Error: ``` ERROR 11-01 04:59:16 multiproc_worker_utils.py:117] Worker VllmWorkerProcess pid 24169 died, exit code: 1 INFO 11-01 04:59:16 multiproc_worker_utils.py:121] Killing local vLLM worker processes Future exception was never retrieved future: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper return func(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner.py", line 1690, in execute_model model_input.async_callback() File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 1125, in weak_bound unbound(inst, *args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 1123, in _process_model_outputs self.output_processor.process_outputs( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/output_processor/single_step.py", line 95, in process_outputs return self._process_sequen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding cuda;operator;quantization;triton buil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: no attribute 'id_to_byte_piece' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug python code: ``` vllm serve mistralai/Mistral-Large-Instruct-2407 \ --tokenizer_mode mistral \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n _process_sequence _group_outputs new_char_count = self.detokenizer.decode_sequence_inplace( File "/usr/local/lib/python3.10/dist-packages/vllm/transformers_utils/detokenizer.py", line 122, in decode_sequence_inplac e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;quantization;speculative_decoding cuda;operator;quantization;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
