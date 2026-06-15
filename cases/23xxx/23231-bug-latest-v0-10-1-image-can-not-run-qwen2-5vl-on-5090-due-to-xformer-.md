# vllm-project/vllm#23231: [Bug]: Latest v0.10.1 image can not run qwen2.5vl on 5090 due to xformer bug

| 字段 | 值 |
| --- | --- |
| Issue | [#23231](https://github.com/vllm-project/vllm/issues/23231) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Latest v0.10.1 image can not run qwen2.5vl on 5090 due to xformer bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug flash attention fails in model initialization. # docker image info ``` docker pull vllm/vllm-openai:v0.10.1 ``` # how to run start vllm with a qwen2.5vl model. A related issue can be found here. https://github.com/Dao-AILab/flash-attention/issues/1763 # output ``` (EngineCore_0 pid=1113) INFO 08-19 20:50:42 [gpu_model_runner.py:2007] Model loading took 15.6269 GiB and 3.074475 seconds (EngineCore_0 pid=1113) INFO 08-19 20:50:42 [gpu_model_runner.py:2591] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. CUDA error (/__w/xformers/xformers/third_party/flash-attention/hopper/flash_fwd_launch_template.h:188): invalid argument (APIServer pid=849) Traceback (most recent call last): (APIServer pid=849) File " ", line 198, in _run_module_as_main (APIServer pid=849) File " ", line 88, in _run_code (APIServer pid=849) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1918, in (APIServer pid=849) uvloop.run(run_server(args)) (APIServer pid=849) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in ru...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### 🐛 Describe the bug flash attention fails in model initialization. # docker image info ``` docker pull vllm/vllm-openai:v0.10.1 ``` # how to run start vllm with a qwen2.5vl model. A related issue can be found here. h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 384 tokens, and profiled with 1 image items of the maximum feature size. CUDA error (/__w/xformers/xformers/third_party/flash-attention/hopper/flash_fwd_launch_template.h:188): invalid argument (APIServer pid=849) Trace...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Latest v0.10.1 image can not run qwen2.5vl on 5090 due to xformer bug bug ### Your current environment ### 🐛 Describe the bug flash attention fails in model initialization. # docker image info ``` docker pull vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: xformer bug bug ### Your current environment ### 🐛 Describe the bug flash attention fails in model initialization. # docker image info ``` docker pull vllm/vllm-openai:v0.10.1 ``` # how to run start vllm with a qwen2.5v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Latest v0.10.1 image can not run qwen2.5vl on 5090 due to xformer bug bug ### Your current environment ### 🐛 Describe the bug flash attention fails in model initialization. # docker image info ``` docker pull vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
