# vllm-project/vllm#17813: [Bug]: 0.8.5 post1 cuda error

| 字段 | 值 |
| --- | --- |
| Issue | [#17813](https://github.com/vllm-project/vllm/issues/17813) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.8.5 post1 cuda error

### Issue 正文摘录

### Your current environment env: 5070ti 16G+5080TI 16G model:Qwen3-32B-AWQ command:PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve xunlei_model/Qwen3-32B-AWQ --port 8099 --max-model-len 25000 --served-model-name vllm --enforce_eager --tensor-parallel-size 2 --gpu_memory_utilization 0.95 A few days ago I installed a relatively new vllm, which allowed me to run tensors in parallel on two graphics cards. A lot of concurrent tests were done at that time and they were successful. But today, I cannot run tensors in parallel. I tried to reinstall vllm but it still doesn't work. (vllmnv) root@epyc:~# pip list |grep torch pytorch-triton 3.3.0+git96316ce5 torch 2.8.0.dev20250507+cu128 torchaudio 2.6.0.dev20250507+cu128 torchvision 0.22.0.dev20250507+cu128 (vllmnv) root@epyc:~# pip list |grep vllm vllm 0.8.5.post2.dev0+g3015d5634.d20250507.cu128 /root/vllmnv (vllmnv) root@epyc:~# pip list |grep triton pytorch-triton 3.3.0+git96316ce5 triton 3.3.0 (vllmnv) root@epyc:~# ### 🐛 Describe the bug (vllmnv) root@epyc:~# PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve xunlei_model/Qwen3-32B-AWQ --port 8099 --max-model-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: -tensor-parallel-size 2 --gpu_memory_utilization 0.95 A few days ago I installed a relatively new vllm, which allowed me to run tensors in parallel on two graphics cards. A lot of concurrent tests were done at that time...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: 0.8.5 post1 cuda error bug;stale ### Your current environment env: 5070ti 16G+5080TI 16G model:Qwen3-32B-AWQ command:PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve xunlei...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: 2B-AWQ command:PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve xunlei_model/Qwen3-32B-AWQ --port 8099 --max-model-len 25000 --served-model-name vllm --enforce_eager --tensor-para...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: 0.8.5 post1 cuda error bug;stale ### Your current environment env: 5070ti 16G+5080TI 16G model:Qwen3-32B-AWQ command:PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve xunlei...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: error bug;stale ### Your current environment env: 5070ti 16G+5080TI 16G model:Qwen3-32B-AWQ command:PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve xunlei_model/Qwen3-32B-AWQ --p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
