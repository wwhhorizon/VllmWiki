# vllm-project/vllm#22884: [Bug]: When deploying the fine-tuned model using vllm, lora loses its effect.

| 字段 | 值 |
| --- | --- |
| Issue | [#22884](https://github.com/vllm-project/vllm/issues/22884) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When deploying the fine-tuned model using vllm, lora loses its effect.

### Issue 正文摘录

### Your current environment vllm==0.8.5.post1 ms_swift== 3.4.0 and 3.7.0 deepspeed==0.16.7 peft==0.15.2 transformers==4.51.3 ### 🐛 Describe the bug I trained a model using Swift, and the results were consistent during training and when running inference using Swift Infer (with a pt backend). The results were also consistent when using Transformers + PEFT for inference. However, after deploying it using vllm serve , the combined model performed the same as before. **vllm deployment code:** vllm serve ./Qwen3_models/merged_model/checkpoint-400-20250814 --port 8000 --max-model-len 16384 **Specific reference:** https://github.com/modelscope/ms-swift/issues/5374 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When deploying the fine-tuned model using vllm, lora loses its effect. bug;stale ### Your current environment vllm==0.8.5.post1 ms_swift== 3.4.0 and 3.7.0 deepspeed==0.16.7 peft==0.15.2 transformers==4.51.3 ### 🐛...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: during training and when running inference using Swift Infer (with a pt backend). The results were also consistent when using Transformers + PEFT for inference. However, after deploying it using vllm serve , the combine...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed_model/checkpoint-400-20250814 --port 8000 --max-model-len 16384 **Specific reference:** https://github.com/modelscope/ms-swift/issues/5374 ### Before submitting a new issue... - [x] Make sure you already searched for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 374 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: en deploying the fine-tuned model using vllm, lora loses its effect. bug;stale ### Your current environment vllm==0.8.5.post1 ms_swift== 3.4.0 and 3.7.0 deepspeed==0.16.7 peft==0.15.2 transformers==4.51.3 ### 🐛 Describe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
