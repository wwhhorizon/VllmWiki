# vllm-project/vllm#3521: [Bug]: An Internal IP exposing maybe a threat

| 字段 | 值 |
| --- | --- |
| Issue | [#3521](https://github.com/vllm-project/vllm/issues/3521) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: An Internal IP exposing maybe a threat

### Issue 正文摘录

### Your current environment While running my vllm code i checked and noticed a self calling interal ip request shown in **netsat** command i.e(netstat -ano). `HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m vllm.entrypoints.openai.api_server --port=5000 --host=127.0.0.1 --model "/home/abc/.cache/huggingface/hub/models--meta-llama--Llama-2-13b-chat-hf/snapshots/c2f3ec81aac798ae26dcc57799a994dfbf521496" --tokenizer=hf-internal-testing/llama-tokenizer --tensor-parallel-size=1 --seed 1234 --max-num-batched-tokens=4096` It shows 192.* series that i dont want. Please try to fix this and provide me a solution and I want my host address 127.0.0.1 should show as my foreign IP instead of my system ip 192.168.100.17 ![vllm_bug](https://github.com/vllm-project/vllm/assets/137979399/5de09872-572b-4c22-9c31-197f641c4c64) while running program and then checking connection througfh netstat it shows localhost with some internal ip as well as 192.168.. ### 🐛 Describe the bug My vllm version is 0.2.2 and I create the vllm conda environment and hit the below command:- `HF_DATASETS_OFFLINE=1` TRANSFORMERS_OFFLINE=1 python -m vllm.entrypoints.openai.api_server --port=5000 --host=127.0.0.1 --mod...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing interal ip request shown in **netsat** command i.e(netstat -ano). `HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m vllm.entrypoints.openai.api_server --port=5000 --host=127.0.0.1 --model "/home/abc/.cache/hug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: h some internal ip as well as 192.168.. ### 🐛 Describe the bug My vllm version is 0.2.2 and I create the vllm conda environment and hit the below command:- `HF_DATASETS_OFFLINE=1` TRANSFORMERS_OFFLINE=1 python -m vllm.e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ile running my vllm code i checked and noticed a self calling interal ip request shown in **netsat** command i.e(netstat -ano). `HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m vllm.entrypoints.openai.api_server...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pshots/c2f3ec81aac798ae26dcc57799a994dfbf521496" --tokenizer=hf-internal-testing/llama-tokenizer --tensor-parallel-size=1 --seed 1234 --max-num-batched-tokens=4096` It shows 192.* series that i dont want. Please try to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
