# vllm-project/vllm#14487: [Bug]: ModuleNotFoundError: No module named 'pyarrow" in main branch

| 字段 | 值 |
| --- | --- |
| Issue | [#14487](https://github.com/vllm-project/vllm/issues/14487) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ModuleNotFoundError: No module named 'pyarrow" in main branch

### Issue 正文摘录

### Your current environment # image info The latest pull request in the repository is "[V1] Prompt logprobs + APC compatibility; prompt logprobs reqs cannot fill APC (#13949)". ![Image](https://github.com/user-attachments/assets/cb1227b4-7048-4219-abc1-c2a5b2d8d48a) # client start shell sudo python3 ./bench_serving.py --backend vllm --dataset-name random --model deepseek-r1 --tokenizer ./tokenizer --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --random-input-len 6000 --random-output-len 1000 --random-range-ratio 1 --request-rate 16 --max-concurrency 16 --num-prompts 80 --base-url $BASE_URL --host 0.0.0.0 --port 8000 --profile # server start shell VLLM_USE_V1=1 VLLM_TORCH_PROFILER_DIR=/disc vllm serve /root/.cache/huggingface --tensor-parallel-size 16 --trust-remote-code --gpu-memory-utilization 0.9 --max-model-len 32768 --enforce-eager --enable-reasoning --reasoning-parser deepseek_r1 --served-model-name deepseek-r1 ## error info ![Image](https://github.com/user-attachments/assets/295c6ce7-04c5-4245-91b2-bc02f9683470) ### 🐛 Describe the bug in the first block ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sudo python3 ./bench_serving.py --backend vllm --dataset-name random --model deepseek-r1 --tokenizer ./tokenizer --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --random-input-len 6000 --random-output-len 100...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ModuleNotFoundError: No module named 'pyarrow" in main branch bug;stale ### Your current environment # image info The latest pull request in the repository is "[V1] Prompt logprobs + APC compatibility; prompt log...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n main branch bug;stale ### Your current environment # image info The latest pull request in the repository is "[V1] Prompt logprobs + APC compatibility; prompt logprobs reqs cannot fill APC (#13949)". ![Image](https://...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -c2a5b2d8d48a) # client start shell sudo python3 ./bench_serving.py --backend vllm --dataset-name random --model deepseek-r1 --tokenizer ./tokenizer --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --random-in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ock ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
