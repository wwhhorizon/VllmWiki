# vllm-project/vllm#14421: [Bug]: low quality of deepseek-vl2 when using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#14421](https://github.com/vllm-project/vllm/issues/14421) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: low quality of deepseek-vl2 when using vllm

### Issue 正文摘录

### 📚 The doc issue When I use the official inference code of deepseek-vl2, the model output seems normal， Question: “图片中的角色是哪部动漫作品中的人物？” ![Image](https://github.com/user-attachments/assets/44dca395-f1dd-4b0c-87d6-d492df512976) Model Output： ![Image](https://github.com/user-attachments/assets/39332703-d613-403d-bcb0-e0cbb8e266d7) But when I use vllm for inference, and I use the [chat_template](https://github.com/vllm-project/vllm/blob/main/examples/template_deepseek_vl2.jinja)，the model output seems abnormal. I start vllm by： `CUDA_VISIBLE_DEVICES=7 vllm serve deepseek-vl2 --port 8102 --max-model-len 4096 --hf_overrides '{"architectures":["DeepseekVLV2ForCausalLM"]}' --gpu-memory-utilization 0.9 --chat_template ./template_deepseek_vl2.jinja` Model Output： ![Image](https://github.com/user-attachments/assets/ea545f6e-fe01-4f67-a50a-65bbed41f86a) I feel that the accuracy has dropped significantly. I don't know if it's a problem with chat_template or somewhere else. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documenta...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e_deepseek_vl2.jinja)，the model output seems abnormal. I start vllm by： `CUDA_VISIBLE_DEVICES=7 vllm serve deepseek-vl2 --port 8102 --max-model-len 4096 --hf_overrides '{"architectures":["DeepseekVLV2ForCausalLM"]}' --g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e doc issue When I use the official inference code of deepseek-vl2, the model output seems normal， Question: “图片中的角色是哪部动漫作品中的人物？” ![Image](https://github.com/user-attachments/assets/44dca395-f1dd-4b0c-87d6-d492df512976)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ttachments/assets/ea545f6e-fe01-4f67-a50a-65bbed41f86a) I feel that the accuracy has dropped significantly. I don't know if it's a problem with chat_template or somewhere else. ### Suggest a potential alternative/fix _N...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ttachments/assets/ea545f6e-fe01-4f67-a50a-65bbed41f86a) I feel that the accuracy has dropped significantly. I don't know if it's a problem with chat_template or somewhere else. ### Suggest a potential alternative/fix _N...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l2 when using vllm documentation ### 📚 The doc issue When I use the official inference code of deepseek-vl2, the model output seems normal， Question: “图片中的角色是哪部动漫作品中的人物？” ![Image](https://github.com/user-attachments/ass...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
