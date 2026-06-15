# vllm-project/vllm#9558: [Bug]: GGUF Llama-3.1-Nemotron-70B-Instruct-HF ValueError: cannot reshape array of size into shape

| 字段 | 值 |
| --- | --- |
| Issue | [#9558](https://github.com/vllm-project/vllm/issues/9558) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GGUF Llama-3.1-Nemotron-70B-Instruct-HF ValueError: cannot reshape array of size into shape

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, when calling the model [Llama-3.1-Nemotron-70B-Instruct-HF-GGUF](https://huggingface.co/bartowski/Llama-3.1-Nemotron-70B-Instruct-HF-GGUF) with the quantization Q6_K and the following args ``` args: default_max_tokens: 4096 model: /models/Llama-3.1-Nemotron-70B-Instruct-HF-Q6_K/Llama-3.1-Nemotron-70B-Instruct-HF-Q6_K-00001-of-00002.gguf dtype: bfloat16 quantization: gguf max_model_len: 8192 tensor_parallel_size: 2 enforce_eager: True gpu_memory_utilization: 0.8 ``` I get this error ``` The deployment failed to start 3 times in a row. This may be due to a problem with its constructor or initial health check failing. See controller logs for details. Retrying after 1 seconds. Error: ray::1 70B completions:vLLMGenericAPI.initialize_and_get_metadata() (pid=3098946, ip=159.103.253.75, actor_id=23d2fed59332cbed1efae01001000000, repr= ) File "/usr/lib64/python3.11/concurrent/futures/_base.py", line 449, in result return self.__get_result() ^^^^^^^^^^^^^^^^^^^ File "/usr/lib64/python3.11/concurrent/futures/_base.py", line 401, in __get_result raise self._exception ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: GGUF Llama-3.1-Nemotron-70B-Instruct-HF ValueError: cannot reshape array of size into shape bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, when calling the model [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ggingface.co/bartowski/Llama-3.1-Nemotron-70B-Instruct-HF-GGUF) with the quantization Q6_K and the following args ``` args: default_max_tokens: 4096 model: /models/Llama-3.1-Nemotron-70B-Instruct-HF-Q6_K/Llama-3.1-Nemot...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: packages/gguf/gguf_reader.py", line 130, in __init__ self._build_tensors(offs, tensors_fields) File "/tmp/runtime_resources/pip/123456789/virtualenv/lib64/python3.11/site-packages/gguf/gguf_reader.py", line 314, in _bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rror: ray::1 70B completions:vLLMGenericAPI.initialize_and_get_metadata() (pid=3098946, ip=159.103.253.75, actor_id=23d2fed59332cbed1efae01001000000, repr= ) File "/usr/lib64/python3.11/concurrent/futures/_base.py", lin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
