# vllm-project/vllm#17455: [Bug]: CalledProcessError: Command '['/usr/local/gcc/bin/gcc', '/tmp/tmpicf7mhq6/main.c', '-O3', '-shared', '-fP

| 字段 | 值 |
| --- | --- |
| Issue | [#17455](https://github.com/vllm-project/vllm/issues/17455) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CalledProcessError: Command '['/usr/local/gcc/bin/gcc', '/tmp/tmpicf7mhq6/main.c', '-O3', '-shared', '-fP

### Issue 正文摘录

### Your current environment cu121+gcc11.2.0，vllm version 0.7.3 ,torch version2.5.1，glibc version2.31 ### 🐛 Describe the bug vllm serve /mnt/hfhub/models--Qwen--Qwen2.5-VL-72B-Instruct \ --dtype auto \ --max_model_len=10240 \ --api-key use-qqwen72b \ --port 20482 \ --served-model-name qwen72b-base \ --gpu-memory-utilization 0.95 \ --tensor-parallel-size 2 and then some error happen: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: CalledProcessError: Command '['/usr/local/gcc/bin/gcc', '/tmp/tmp8vajoenb/main.c', '-O3', '-shared', '-fPIC', '-o', '/tmp/tmp8vajoenb/cuda_utils.cpython-310-x86_64-linux-gnu.so', '-lcuda', '-L/mnt/petrelfs/anaconda3/envs/cuda118_vllm/lib/python3.10/site-packages/triton/backends/nvidia/lib', '-L/.singularity.d/libs', '-I/mnt/petrelfs/anaconda3/envs/cuda118_vllm/lib/python3.10/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp8vajoenb', '-I/mnt/petrelfs/anaconda3/envs/cuda118_vllm/include/python3.10']' returned non-zero exit status 1. Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ared', '-fP bug;stale ### Your current environment cu121+gcc11.2.0，vllm version 0.7.3 ,torch version2.5.1，glibc version2.31 ### 🐛 Describe the bug vllm serve /mnt/hfhub/models--Qwen--Qwen2.5-VL-72B-Instruct \ --dtype au...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: version2.5.1，glibc version2.31 ### 🐛 Describe the bug vllm serve /mnt/hfhub/models--Qwen--Qwen2.5-VL-72B-Instruct \ --dtype auto \ --max_model_len=10240 \ --api-key use-qqwen72b \ --port 20482 \ --served-model-name qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --tensor-parallel-size 2 and then some error happen: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: CalledProcessError: Command '['/usr/local/gcc/bin/gcc', '/tmp/tmp8vajoenb/main.c', '-O3', '-shared...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /tmp8vajoenb/main.c', '-O3', '-shared', '-fPIC', '-o', '/tmp/tmp8vajoenb/cuda_utils.cpython-310-x86_64-linux-gnu.so', '-lcuda', '-L/mnt/petrelfs/anaconda3/envs/cuda118_vllm/lib/python3.10/site-packages/triton/backends/n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e bug vllm serve /mnt/hfhub/models--Qwen--Qwen2.5-VL-72B-Instruct \ --dtype auto \ --max_model_len=10240 \ --api-key use-qqwen72b \ --port 20482 \ --served-model-name qwen72b-base \ --gpu-memory-utilization 0.95 \ --ten...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
