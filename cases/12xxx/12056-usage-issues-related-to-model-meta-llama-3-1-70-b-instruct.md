# vllm-project/vllm#12056: [Usage]: Issues related to model meta llama 3.1 70 b instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#12056](https://github.com/vllm-project/vllm/issues/12056) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Issues related to model meta llama 3.1 70 b instruct

### Issue 正文摘录

### Your current environment .. ### How would you like to use vllm Hello everyone, I have been trying to deploy the model meta-llama/Llama-3.1-70B-Instruct for the pass few days. I am trying to deploy it on Runpod through Vllm. I am using 4xA40 GPU=192GB. This is the configuration "--host 0.0.0.0 --port 8000 --model meta-llama/Llama-3.1-70B-Instruct --dtype bfloat16 --enforce-eager --gpu-memory-utilization 0.95 --api-key sk-IrR7Bwxtin0haWagUnPrBgq5PurnUz86 --max-model-len 8128 --tensor-parallel-size 4 " Using the above, when i deploy, i am getting these messages ![Image](https://github.com/user-attachments/assets/87ddbc90-b4b2-439d-8ca3-bd6847466838) you can see the image, it says model is being download and load. However, it stays still like this as long as i leave it. Even I waited upto 1 hour. ![Image](https://github.com/user-attachments/assets/e602791b-b302-4abb-b10d-59289a84a249) I HAVE ADDED THIS PICTURE FOR THE REFERENCE AS WELL. if the model load fully, the container volume should increase upto 80%, but it stays still at 16%. I have tried other models with this configuration like meta llama 3.1 8b, meta llama 3.q 70B-qunatized, they all work fine what is the issue here. PL...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: "--host 0.0.0.0 --port 8000 --model meta-llama/Llama-3.1-70B-Instruct --dtype bfloat16 --enforce-eager --gpu-memory-utilization 0.95 --api-key sk-IrR7Bwxtin0haWagUnPrBgq5PurnUz86 --max-model-len 8128 --tensor-parallel-s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Issues related to model meta llama 3.1 70 b instruct usage;stale ### Your current environment .. ### How would you like to use vllm Hello everyone, I have been trying to deploy the model meta-llama/Llama-3.1-70...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: elp ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Issues related to model meta llama 3.1 70 b instruct usage;stale ### Your current environment .. ### How would you like to use vllm Hello everyone, I have been trying to deploy the model meta-llama/Llama-3.1-70...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
