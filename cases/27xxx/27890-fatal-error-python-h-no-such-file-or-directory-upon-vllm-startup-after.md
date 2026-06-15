# vllm-project/vllm#27890: "fatal error: Python.h: No such file or directory" upon vllm startup after a clean install

| 字段 | 值 |
| --- | --- |
| Issue | [#27890](https://github.com/vllm-project/vllm/issues/27890) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> "fatal error: Python.h: No such file or directory" upon vllm startup after a clean install

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After a clean installation of vllm on Ubuntu 24.04 LTS with RTX 5090 by [following official guide](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#set-up-using-python): ``` uv venv --python 3.12 --seed source .venv/bin/activate uv pip install vllm --torch-backend=auto ``` ... I started vllm and can see this: ``` # vllm serve models/Qwen3-4B-Thinking-2507 INFO 10-31 16:03:43 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=15408) INFO 10-31 16:03:47 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=15408) INFO 10-31 16:03:47 [utils.py:233] non-default args: {'model_tag': 'models/Qwen3-4B-Thinking-2507', 'model': 'models/Qwen3-4B-Thinking-2507'} (APIServer pid=15408) INFO 10-31 16:03:51 [model.py:547] Resolved architecture: Qwen3ForCausalLM (APIServer pid=15408) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=15408) INFO 10-31 16:03:51 [model.py:1510] Using max model len 262144 (APIServer pid=15408) INFO 10-31 16:03:51 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 10-31 16:03:53 [__init__.py:216] Automatically detecte...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: or: Python.h: No such file or directory" upon vllm startup after a clean install bug;unstale ### Your current environment ### 🐛 Describe the bug After a clean installation of vllm on Ubuntu 24.04 LTS with RTX 5090 by [f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: python 3.12 --seed source .venv/bin/activate uv pip install vllm --torch-backend=auto ``` ... I started vllm and can see this: ``` # vllm serve models/Qwen3-4B-Thinking-2507
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: No such file or directory" upon vllm startup after a clean install bug;unstale ### Your current environment ### 🐛 Describe the bug After a clean installation of vllm on Ubuntu 24.04 LTS with RTX 5090 by [following offic...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: (APIServer pid=15408) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=1
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: h-backend=auto ``` ... I started vllm and can see this: ``` # vllm serve models/Qwen3-4B-Thinking-2507 INFO 10-31 16:03:43 [__init__.py

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
