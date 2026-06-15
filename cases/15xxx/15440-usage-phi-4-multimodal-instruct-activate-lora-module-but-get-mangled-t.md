# vllm-project/vllm#15440: [Usage]: `Phi-4-multimodal-instruct` activate LoRA module but get mangled text output

| 字段 | 值 |
| --- | --- |
| Issue | [#15440](https://github.com/vllm-project/vllm/issues/15440) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: `Phi-4-multimodal-instruct` activate LoRA module but get mangled text output

### Issue 正文摘录

### Your current environment ### How would you like to use vllm ### 🐛 Describe the bug I deployed `Phi-4-multimodal-instruct` by using the this cmd and activating its audio function only: ```shell NCCL_CUMEM_ENABLE=0 NCCL_DEBUG=TRACE CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1,5 vllm serve /my/path/to/models/Huggingface_download/Phi-4-multimodal-instruct --task generate --trust-remote-code --limit-mm-per-prompt audio=10 --tensor-parallel-size 2 --gpu-memory-utilization 0.99 --port 8007 --max_num_seqs 1 --enable_lora --max_lora_rank 320 --lora-modules speech=/my/path/to/models/Huggingface_download/Phi-4-multimodal-instruct/speech-lora ``` Then I prompt it in Chinese with a "audio+text -> text" task. And I found out the output of model is all mangled text. But when I disabled lora and redeployed it: ``` NCCL_CUMEM_ENABLE=0 NCCL_DEBUG=TRACE CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1,5 vllm serve /my/path/to/models/Huggingface_download/Phi-4-multimodal-instruct --task generate --trust-remote-code --limit-mm-per-prompt audio=10 --tensor-parallel-size 2 --gpu-memory-utilization 0.99 --port 8007 --max_num_seqs 1 ``` I found everything ran well and it correctly answered me in Chinese...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: `Phi-4-multimodal-instruct` activate LoRA module but get mangled text output usage;stale ### Your current environment ### How would you like to use vllm ### 🐛 Describe the bug I deployed `Phi-4-multimodal-instr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;trito...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g its audio function only: ```shell NCCL_CUMEM_ENABLE=0 NCCL_DEBUG=TRACE CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1,5 vllm serve /my/path/to/models/Huggingface_download/Phi-4-multimodal-instruct --task generate --tru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: timodal-instruct` activate LoRA module but get mangled text output usage;stale ### Your current environment ### How would you like to use vllm ### 🐛 Describe the bug I deployed `Phi-4-multimodal-instruct` by using the t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
