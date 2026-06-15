# vllm-project/vllm#12371: [Bug]: [TPU] Prefix caching + w8a8 + long context results in degraded performance and corrupted output

| 字段 | 值 |
| --- | --- |
| Issue | [#12371](https://github.com/vllm-project/vllm/issues/12371) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [TPU] Prefix caching + w8a8 + long context results in degraded performance and corrupted output

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Model: https://huggingface.co/neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8 Machine: TPU v6e-8 Image: vlm/vllm-tpu:2fc6944c5e69d5d0ce15d09a855452c795d75c3c I would suggest running this in the TPU VM using tmux First, start the server ``` docker run --privileged -it --network host --rm -v /dev/shm:/data -e HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN} -e VLLM_XLA_CACHE_PATH=/data/jax --shm-size=10.24gb vllm/vllm-tpu:2fc6944c5e69d5d0ce15d09a855452c795d75c3c python3 -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8000 --tensor-parallel-size=8 --max-model-len=65536 --gpu-memory-utilization=0.75 --max-num-seqs=32 --model=neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8 --download-dir /data --disable-log-requests --enable_prefix_caching ``` Run the benchmark from another container instance (tmux pane) ``` docker run -it --rm --network host vllm/vllm-tpu:2fc6944c5e69d5d0ce15d09a855452c795d75c3c python3 -m pip install -r requirements-test.txt cd benchmarks python3 benchmark_serving.py --model neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8 --dataset-name sonnet --da...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: erformance and corrupted output bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Model: https://huggingface.co/neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8 Machine: T...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ggest running this in the TPU VM using tmux First, start the server ``` docker run --privileged -it --network host --rm -v /dev/shm:/data -e HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN} -e VLLM_XLA_CACHE_PATH=/data/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ad-dir /data --disable-log-requests --enable_prefix_caching ``` Run the benchmark from another container instance (tmux pane) ``` docker run -it --rm --network host vllm/vllm-tpu:2fc6944c5e69d5d0ce15d09a855452c795d75c3c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g Model: https://huggingface.co/neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8 Machine: TPU v6e-8 Image: vlm/vllm-tpu:2fc6944c5e69d5d0ce15d09a855452c795d75c3c I would suggest running this in the TPU VM using tmu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
