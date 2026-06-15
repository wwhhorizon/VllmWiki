# vllm-project/vllm#24038: [Bug]: vLLM >V0.9.2 with AWQ model producing nonsense in longer context chats 

| 字段 | 值 |
| --- | --- |
| Issue | [#24038](https://github.com/vllm-project/vllm/issues/24038) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM >V0.9.2 with AWQ model producing nonsense in longer context chats 

### Issue 正文摘录

### Your current environment I'm using this model https://huggingface.co/gghfez/c4ai-command-a-03-2025-AWQ It's an AWQ quant of the Cohere Command A model. I'm running the latest vLLM v0.10.1.1 and v0.9.2 in Docker on PopOS 22.04 ### 🐛 Describe the bug With vLLM v0.9.2 inference works perfectly fine out of the box. But with the latest vLLM (v0.10.1.1) with a chat above 20k tokens this model produces endless repeating special characters. example: "ــ |ــ |ــ | | |ــ | | |ــ |ــ | | | | | | | | | |ــ | | |ــ | | | | | | | | | | | | | | | | |" Short chats work without issues. How can I debug or mediate the cause of this issue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM >V0.9.2 with AWQ model producing nonsense in longer context chats bug;stale ### Your current environment I'm using this model https://huggingface.co/gghfez/c4ai-command-a-03-2025-AWQ It's an AWQ quant of the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: vLLM >V0.9.2 with AWQ model producing nonsense in longer context chats bug;stale ### Your current environment I'm using this model https://huggingface.co/gghfez/c4ai-command-a-03-2025-AWQ It's an AWQ quant of the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: del https://huggingface.co/gghfez/c4ai-command-a-03-2025-AWQ It's an AWQ quant of the Cohere Command A model. I'm running the latest vLLM v0.10.1.1 and v0.9.2 in Docker on PopOS 22.04 ### 🐛 Describe the bug With vLLM v0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: M >V0.9.2 with AWQ model producing nonsense in longer context chats bug;stale ### Your current environment I'm using this model https://huggingface.co/gghfez/c4ai-command-a-03-2025-AWQ It's an AWQ quant of the Cohere Co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
