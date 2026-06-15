# vllm-project/vllm#1937: Error when performing `benchmarks/benchmark_latency.py` using multiple GPUs on a single node

| 字段 | 值 |
| --- | --- |
| Issue | [#1937](https://github.com/vllm-project/vllm/issues/1937) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error when performing `benchmarks/benchmark_latency.py` using multiple GPUs on a single node

### Issue 正文摘录

Hi! I am evaluating various server's latency and I hit road block. Steps I did to prepare ```bash echo "export HF_HUB_ENABLE_HF_TRANSFER=1" >> ~/.bashrc echo "export PIP_DISABLE_PIP_VERSION_CHECK=1" >> ~/.bashrc source ~/.bashrc export HUGGING_FACE_HUB_TOKEN=ht---- pip install vllm hf_transfer pip install --upgrade torch # had errors on some servers git clone https://github.com/vllm-project/vllm.git cd vllm # to change the hardcoded limit that is 32k and will otherwise cause OOM sed -i '24i\ max_model_len=8192' benchmarks/benchmark_latency.py export MODEL="ehartford/dolphin-2.1-mistral-7b" huggingface-cli download $MODEL ``` Single GPU benchmark WORKS ``` python benchmarks/benchmark_latency.py --model $MODEL \ --input-len 1000 --output-len 100 \ --n 2 --batch-size 1 --num-iters 10 ``` Multiple GPU benchmark ERROR ``` pip install ray ray start --head ray start --address='192.168.122.113:6379' python benchmarks/benchmark_latency.py --model $MODEL \ --input-len 1000 --output-len 100 \ --n 2 --batch-size 1 --num-iters 10 -tp 2 ``` Multiple GPU inference WORKS ```bash python -m vllm.entrypoints.openai.api_server \ --model $MODEL \ --host 0.0.0.0 --port 8888 \ --max-model-len 8192 -tp 2...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tency and I hit road block. Steps I did to prepare ```bash echo "export HF_HUB_ENABLE_HF_TRANSFER=1" >> ~/.bashrc echo "export PIP_DISABLE_PIP_VERSION_CHECK=1" >> ~/.bashrc source ~/.bashrc export HUGGING_FACE_HUB_TOKEN...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Error when performing `benchmarks/benchmark_latency.py` using multiple GPUs on a single node Hi! I am evaluating various server's latency and I hit road block. Steps I did to prepare ```bash echo "export HF_HUB_ENABLE_H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t HF_HUB_ENABLE_HF_TRANSFER=1" >> ~/.bashrc echo "export PIP_DISABLE_PIP_VERSION_CHECK=1" >> ~/.bashrc source ~/.bashrc export HUGGING_FACE_HUB_TOKEN=ht---- pip install vllm hf_transfer pip install --upgrade torch # had...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: llm # to change the hardcoded limit that is 32k and will otherwise cause OOM sed -i '24i\ max_model_len=8192' benchmarks/benchmark_latency.py export MODEL="ehartford/dolphin-2.1-mistral-7b" huggingface-cli download $MOD...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: single node Hi! I am evaluating various server's latency and I hit road block. Steps I did to prepare ```bash echo "export HF_HUB_ENABLE_HF_TRANSFER=1" >> ~/.bashrc echo "export PIP_DISABLE_PIP_VERSION_CHECK=1" >> ~/.ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
