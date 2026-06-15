# vllm-project/vllm#8669: [Bug]: Slow Inference Speed with llama 3.1 70B GGUF Q4 on A100 80G (8.7 tokens/s)

| 字段 | 值 |
| --- | --- |
| Issue | [#8669](https://github.com/vllm-project/vllm/issues/8669) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Slow Inference Speed with llama 3.1 70B GGUF Q4 on A100 80G (8.7 tokens/s)

### Issue 正文摘录

### Your current environment I am running the llama 3.1 70B GGUF Q4 model on an A100 80G GPU using vLLM. However, the inference speed is significantly slower than expected, reaching only 8.7 tokens per second. ### Model Input Dumps here is my command to start the sevice ```bash (vllm) root@C.12616778:~$ vllm serve ./Meta-Llama-3.1-70B-Instruct-Q4_K_M.gguf --tokenizer unsloth/Meta-Llama-3.1-70B-Instruct --max-model-len 8192 ``` some print ![image](https://github.com/user-attachments/assets/00a62276-e051-40e5-b6fc-f3d362b986ca) ![image](https://github.com/user-attachments/assets/b1fbc2c5-831d-4c1a-afa2-2817919a025f) ### 🐛 Describe the bug here is my inference speed ![image](https://github.com/user-attachments/assets/72da37b4-3956-430a-a14e-4c779fd90d0e) Is this speed normal for this model and hardware setup, or could there be an problem with my configuration? I wonder if I missed something during setup or optimization that could improve the performance. Thank you very much!! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Slow Inference Speed with llama 3.1 70B GGUF Q4 on A100 80G (8.7 tokens/s) bug;stale ### Your current environment I am running the llama 3.1 70B GGUF Q4 model on an A100 80G GPU using vLLM. However, the inference...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Slow Inference Speed with llama 3.1 70B GGUF Q4 on A100 80G (8.7 tokens/s) bug;stale ### Your current environment I am running the llama 3.1 70B GGUF Q4 model on an A100 80G GPU using vLLM. However, the inference...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 8:~$ vllm serve ./Meta-Llama-3.1-70B-Instruct-Q4_K_M.gguf --tokenizer unsloth/Meta-Llama-3.1-70B-Instruct --max-model-len 8192 ``` some print ![image](https://github.com/user-attachments/assets/00a62276-e051-40e5-b6fc-f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nference Speed with llama 3.1 70B GGUF Q4 on A100 80G (8.7 tokens/s) bug;stale ### Your current environment I am running the llama 3.1 70B GGUF Q4 model on an A100 80G GPU using vLLM. However, the inference speed is sig...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
