# vllm-project/vllm#21175: [Bug]: Wrongly reuse KV, for V1 PD disaggregation with multimodal input

| 字段 | 值 |
| --- | --- |
| Issue | [#21175](https://github.com/vllm-project/vllm/issues/21175) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Wrongly reuse KV, for V1 PD disaggregation with multimodal input

### Issue 正文摘录

### Your current environment / ### 🐛 Describe the bug **I use the model Qwen2.5-VL-3B-Instruct for V1 PD disaggregation with 1 image input; Everything is fine until I sent 2 different requests, with identical text prompt, but different input images in same image size. It wrongly reuses KV for the later request, which cause it wrongly returning an identical output with the previous request.** **I use the `SharedStorageConnector` to faciliate the v1 PD disagg; but I guess there is no design/implementation for this issue yet for other connector as well?** I tried these requests in a single instance (PD mix) case, and a 1P1D disaggregation case in V1. The outputs in PD disagg are similar/identical to the outputs from PD mix; Prefiller encode the mm_input, then prefill, then Decoder can successfully load KV stored from Prefiller and give decent results. I think we can assume that V1 PD disagg with mm input works fine in general, _except for below bug situation: ```python # prompt: # {"type": "text", "text": "Repeat all below: What is following the sequence 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71? Repeat the whole sequence;...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Wrongly reuse KV, for V1 PD disaggregation with multimodal input bug ### Your current environment / ### 🐛 Describe the bug **I use the model Qwen2.5-VL-3B-Instruct for V1 PD disaggregation with 1 image input; Eve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: egation with 1 image input; Everything is fine until I sent 2 different requests, with identical text prompt, but different input images in same image size. It wrongly reuses KV for the later request, which cause it wro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: with the previous request.** **I use the `SharedStorageConnector` to faciliate the v1 PD disagg; but I guess there is no design/implementation for this issue yet for other connector as well?** I tried these requests in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: return 0 || return 1 } # prefilling instance, which is the KV producer CUDA_VISIBLE_DEVICES=0 vllm serve $MODEL_NAME \ --port 7104 \ --gpu-memory-utilization 0.8 \ --trust-remote-code \ --kv-transfer-config \ '{"kv_conn...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dn't find any design specifically for multimodal V1 PD disagg?** ### To reproduce: vllm version: v0.9.2 To start the PD instances: ```python MODEL_NAME=models/Qwen2.5-VL-3B-Instruct/ # model path here # a function that...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
