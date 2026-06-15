# vllm-project/vllm#7946: [Bug]: deploy multi lora by vllm mode error

| 字段 | 值 |
| --- | --- |
| Issue | [#7946](https://github.com/vllm-project/vllm/issues/7946) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deploy multi lora by vllm mode error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug in T4 and vllm version==0.4.3 deploy multi lora by vllm failed, error info: RuntimeError: CUDA error: no kernel image is available for execution on the device. my deploy command: CUDA_VISIBLE_DEVICES=0,1,2,3 swift deploy --tensor_parallel_size 4 --dtype fp16 --model_type qwen1half-7b-chat --model_id_or_path /cloud/user/data/data0806/llm/M2/Chat_New --ckpt_dir /cloud/user/data/data0806/llm/M2/checkpoint-200/ --infer_back vllm -- vllm_enable_lora true --max_model_len 512 --enforce_eager I tried to vllm to 0.5.5, there is still error ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rsion==0.4.3 deploy multi lora by vllm failed, error info: RuntimeError: CUDA error: no kernel image is available for execution on the device. my deploy command: CUDA_VISIBLE_DEVICES=0,1,2,3 swift deploy --tensor_parall...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: BLE_DEVICES=0,1,2,3 swift deploy --tensor_parallel_size 4 --dtype fp16 --model_type qwen1half-7b-chat --model_id_or_path /cloud/user/data/data0806/llm/M2/Chat_New --ckpt_dir /cloud/user/data/data0806/llm/M2/checkpoint-2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Your current environment ### 🐛 Describe the bug in T4 and vllm version==0.4.3 deploy multi lora by vllm failed, error info: RuntimeError: CUDA error: no kernel image is available for execution on the device. my depl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nd: CUDA_VISIBLE_DEVICES=0,1,2,3 swift deploy --tensor_parallel_size 4 --dtype fp16 --model_type qwen1half-7b-chat --model_id_or_path /cloud/user/data/data0806/llm/M2/Chat_New --ckpt_dir /cloud/user/data/data0806/llm/M2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: deploy multi lora by vllm mode error bug;stale ### Your current environment ### 🐛 Describe the bug in T4 and vllm version==0.4.3 deploy multi lora by vllm failed, error info: RuntimeError: CUDA error: no kernel i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
