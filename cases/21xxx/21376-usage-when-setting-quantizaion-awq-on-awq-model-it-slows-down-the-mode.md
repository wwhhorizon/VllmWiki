# vllm-project/vllm#21376: [Usage]: when setting quantizaion AWQ on AWQ model it slows down the model execution by up to 5x

| 字段 | 值 |
| --- | --- |
| Issue | [#21376](https://github.com/vllm-project/vllm/issues/21376) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: when setting quantizaion AWQ on AWQ model it slows down the model execution by up to 5x

### Issue 正文摘录

### Your current environment using docker: vllm/vllm-openai:latest (0.9.2) ### 🐛 Describe the bug I noticed that when specifying quantization awq on the docker params, with the param the model will get up to 5x less token generation speed. Does this make any sense? ex: ``` export MODEL_ID=hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 docker run \ -e VLLM_USE_V1=1 \ --ipc=host \ -p "${MODEL_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "VLLM_LOGGING_LEVEL=${VLLM_LOGGING_LEVEL}" \ -v "${HF_HOME}:/root/.cache/huggingface" \ -v ~/.cache/vllm/torch_compile_cache:/root/.cache/vllm/torch_compile_cache \ vllm/vllm-openai:latest \ --model ${MODEL_ID} \ --tokenizer hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 \ --max-model-len 8192 \ --quantization awq ``` with --quantization awq I get Total Token Throughput of 23 t/s, removing the parameter gives me 123 t/s testing with vllm benchmarks ``` python benchmarks/benchmark_serving.py ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: when setting quantizaion AWQ on AWQ model it slows down the model execution by up to 5x usage ### Your current environment using docker: vllm/vllm-openai:latest (0.9.2) ### 🐛 Describe the bug I noticed that whe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: he model execution by up to 5x usage ### Your current environment using docker: vllm/vllm-openai:latest (0.9.2) ### 🐛 Describe the bug I noticed that when specifying quantization awq on the docker params, with the param...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 5x usage ### Your current environment using docker: vllm/vllm-openai:latest (0.9.2) ### 🐛 Describe the bug I noticed that when specifying quantization awq on the docker params, with the param the model will get up to 5x...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: when setting quantizaion AWQ on AWQ model it slows down the model execution by up to 5x usage ### Your current environment using docker: vllm/vllm-openai:latest (0.9.2) ### 🐛 Describe the bug I noticed that whe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
