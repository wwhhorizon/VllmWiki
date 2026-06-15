# vllm-project/vllm#11167: [Bug]: "Successful requests" in the results is  lower than the value set for the --num-prompts parameter.

| 字段 | 值 |
| --- | --- |
| Issue | [#11167](https://github.com/vllm-project/vllm/issues/11167) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "Successful requests" in the results is  lower than the value set for the --num-prompts parameter.

### Issue 正文摘录

### Your current environment vllm 0.6.4 post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using benchmark_serving.py for online inference benchmarking, the number of "Successful requests" in the results is typically lower than the value set for the --num-prompts parameter. example: python benchmark_serving.py --backend vllm --dataset="ShareGPT_V3_unfiltered_cleaned_split.json" --model "/local/models/Qwen2-72B-Instruct" --host "localhost" --port "8000" --num-prompts 50 --seed 1100 ![image](https://github.com/user-attachments/assets/cf58c4b1-986c-4e78-aa03-a31c388a8511) when --num-prompts 100 , Successful requests: 97 but in api server log, no errors reports. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: parameter. bug;stale ### Your current environment vllm 0.6.4 post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using benchmark_serving.py for online inference benchmarking, the number of "Successful...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: "Successful requests" in the results is lower than the value set for the --num-prompts parameter. bug;stale ### Your current environment vllm 0.6.4 post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using benchmark_serving.py for online inference benchmarking, the number of "Successful requests" in the results is typically lower than the value set for...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: for the --num-prompts parameter. example: python benchmark_serving.py --backend vllm --dataset="ShareGPT_V3_unfiltered_cleaned_split.json" --model "/local/models/Qwen2-72B-Instruct" --host "localhost" --port "8000" --nu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
