# vllm-project/vllm#8142: [Bug]: Using the same startup command, deepseek-v2-lite succeeds while deepseek-v2 236b encounters an error.

| 字段 | 值 |
| --- | --- |
| Issue | [#8142](https://github.com/vllm-project/vllm/issues/8142) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using the same startup command, deepseek-v2-lite succeeds while deepseek-v2 236b encounters an error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` bash python3 -m vllm.entrypoints.openai.api_server --model $LOCAL_PATH --served-model-name dsv2 --trust-remote-code --tensor-parallel-size 8 --max-model-len 8192 --port $PORT0 --dtype bfloat16 --root-path $ROUTE_PATH --gpu-memory-utilization 0.9 --cpu-offload-gb 35 ``` with LOCAL_PATH= path of deepseek-v2-lite-instruct ``` Normal startup ``` with LOCAL_PATH= path of deepseek-v2-instruct ``` ERROR 09-04 11:48:37 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 15570 died, exit code: -15 INFO 09-04 11:48:37 multiproc_worker_utils.py:123] Killing local vLLM worker processes Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap self.run() File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.9/dist-packages/vllm/entrypoints/openai/rpc/server.py", line 230, in run_rpc_server server = AsyncEngineRPCServer(async_engine_args, usage_context, rpc_path) File "/usr/local/lib/python3.9/dist-packages/vllm/entrypoints/openai/rpc/server.py", line 31, in __init__...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. /usr/lib/python3.9/multiprocessing/resource_tracker.py:216: UserWarning: resou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: emote-code --tensor-parallel-size 8 --max-model-len 8192 --port $PORT0 --dtype bfloat16 --root-path $ROUTE_PATH --gpu-memory-utilization 0.9 --cpu-offload-gb 35 ``` with LOCAL_PATH= path of deepseek-v2-lite-instruct ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ages/vllm/model_executor/layers/fused_moe/layer.py", line 99, in forward_cuda return fused_experts(hidden_states=x, File "/usr/local/lib/python3.9/dist-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 5...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: els/deepseek_v2.py", line 148, in forward final_hidden_states = self.experts( File "/usr/local/lib/python3.9/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: scribe the bug ``` bash python3 -m vllm.entrypoints.openai.api_server --model $LOCAL_PATH --served-model-name dsv2 --trust-remote-code --tensor-parallel-size 8 --max-model-len 8192 --port $PORT0 --dtype bfloat16 --root-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
