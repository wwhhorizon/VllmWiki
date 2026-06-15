# vllm-project/vllm#24430: [Bug]: torch.AcceleratorError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#24430](https://github.com/vllm-project/vllm/issues/24430) |
| 状态 | open |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.AcceleratorError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to deploy `Qwen2VLForConditionalGeneration` using vllm, both tried 0.10.0 and nightly version, all failed on some machine. I run it on 10 L20 instances, 4 of them failed to start. The model is [Qwen2-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) My cmd is ``` vllm serve /opt/models/mm_embedding_2b --trust-remote-code --swap-space 16 --disable-log-requests --port 9491 --host :: --dtype bfloat16 --limit-mm-per-prompt '{"image":1,"video":1}' --task embed --tensor-parallel-size 1 --max-model-len 4096 --override-pooler-config '{"pooling_type":"LAST","normalize":false}' --chat-template /opt/models/mm_embedding_2b/embedding_template.jinja2 --enforce-eager ``` The error is ``` (EngineCore_0 pid=713790) ERROR 09-08 09:02:44 [core.py:718] self.model_executor = executor_class(vllm_config) (EngineCore_0 pid=713790) ERROR 09-08 09:02:44 [core.py:718] File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 54, in __init__ (EngineCore_0 pid=713790) ERROR 09-08 09:02:44 [core.py:718] self._init_executor() (EngineCore_0 pid=713790) ERROR 09-08 09:02:44 [core.py:718] File "/usr/local/lib/python...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ## Your current environment ### 🐛 Describe the bug I try to deploy `Qwen2VLForConditionalGeneration` using vllm, both tried 0.10.0 and nightly version, all failed on some machine. I run it on 10 L20 instances, 4 of them...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en2VLForConditionalGeneration` using vllm, both tried 0.10.0 and nightly version, all failed on some machine. I run it on 10 L20 instances, 4 of them failed to start. The model is [Qwen2-VL-2B-Instruct](https://huggingf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: mote-code --swap-space 16 --disable-log-requests --port 9491 --host :: --dtype bfloat16 --limit-mm-per-prompt '{"image":1,"video":1}' --task embed --tensor-parallel-size 1 --max-model-len 4096 --override-pooler-config '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: torch.AcceleratorError: CUDA error: an illegal memory access was encountered bug ### Your current environment ### 🐛 Describe the bug I try to deploy `Qwen2VLForConditionalGeneration` using vllm, both tried 0.10.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: models/mm_embedding_2b --trust-remote-code --swap-space 16 --disable-log-requests --port 9491 --host :: --dtype bfloat16 --limit-mm-per-prompt '{"image":1,"video":1}' --task embed --tensor-parallel-size 1 --max-model-le...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
