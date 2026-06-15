# vllm-project/vllm#12956: [Bug]: VLLM_USE_V1=1 failed with deepseek-v3

| 字段 | 值 |
| --- | --- |
| Issue | [#12956](https://github.com/vllm-project/vllm/issues/12956) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM_USE_V1=1 failed with deepseek-v3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### command ``` VLLM_USE_V1=1 \ vllm serve models/hf_hub/models--deepseek-ai--DeepSeek-V3/snapshots/4c1f24cc10a2a1894304c7ab52edd9710c047571 \ --enforce-eager \ --trust-remote-code \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 ``` ### error log ``` 2025-02-08 10:06:05,206 ERROR worker.py:422 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.execute_method() (pid=8701, ip=200.18.62.194, actor_id=3136656f23b653f477440ad202000000, repr= ) File "/opt/vllm/vllm/worker/worker_base.py", line 575, in execute_method raise e File "/opt/vllm/vllm/worker/worker_base.py", line 566, in execute_method return run_method(target, method, args, kwargs) File "/opt/vllm/vllm/utils.py", line 2220, in run_method return func(*args, **kwargs) File "/opt/vllm/vllm/v1/worker/gpu_worker.py", line 143, in load_model self.model_runner.load_model() File "/opt/vllm/vllm/v1/worker/gpu_model_runner.py", line 869, in load_model self.model = get_model(vllm_config=self.vllm_config) File "/opt/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model return loader.load_model(vllm_config=vllm_config) Fi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support attention;cuda;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t ### 🐛 Describe the bug ### command ``` VLLM_USE_V1=1 \ vllm serve models/hf_hub/models--deepseek-ai--DeepSeek-V3/snapshots/4c1f24cc10a2a1894304c7ab52edd9710c047571 \ --enforce-eager \ --trust-remote-code \ --tensor-pa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lf.impl = impl_cls(num_heads, head_size, scale, num_kv_heads, TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'q_lora_rank' ``` ### Before submitting a new issue... - [x] Make sure you alread...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: y", line 115, in __init__ self.impl = impl_cls(num_heads, head_size, scale, num_kv_heads, TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'q_lora_rank' ``` ### Before submitting a new issue.....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
