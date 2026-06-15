# vllm-project/vllm#8176: [Performance]: reproducing vLLM performance benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#8176](https://github.com/vllm-project/vllm/issues/8176) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: reproducing vLLM performance benchmark

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance To reproduce vLLM's performance benchmark, please launch a shell in the following docker images: - SGlang: `lmsysorg/sglang:v0.3.0-cu124` - lmdeploy: `openmmlab/lmdeploy:v0.6.0a0-cu12` - TensorRT-LLM: `nvcr.io/nvidia/tritonserver:24.07-trtllm-python-py3` - vLLM: `vllm/vllm-openai:v0.6.0` And then run the following bash script (don't forget to replace with your huggingface token that has Llama-3 model access): ```bash export HF_TOKEN= apt update apt install -y wget unzip # download benchmarking code wget -O benchmarking_code.zip https://buildkite.com/organizations/vllm/pipelines/performance-benchmark/builds/8532/jobs/0191bbbf-c603-4c15-9f5d-e0b2933ba097/artifacts/0191bd2a-d6cd-4f6d-b618-a7aa2c39456c unzip benchmarking_code.zip # remove previous results rm -r ./benchmarks/results VLLM_SOURCE_CODE_LOC=$(pwd) bash .buildkite/nightly-benchmarks/scripts/run-nightly-benchmarks.sh ``` Your benchmarking results will be in `./benchmarks/results`, with the name format of `xxx_nightly_results.json `and can be loaded and converted to pandas dataframe by `panda...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Performance]: reproducing vLLM performance benchmark performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance To reproduc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: then run the following bash script (don't forget to replace with your huggingface token that has Llama-3 model access): ```bash export HF_TOKEN= apt update apt install -y wget unzip # download benchmarking code wget -O...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: reproducing vLLM performance benchmark performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance To reproduc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ploy: `openmmlab/lmdeploy:v0.6.0a0-cu12` - TensorRT-LLM: `nvcr.io/nvidia/tritonserver:24.07-trtllm-python-py3` - vLLM: `vllm/vllm-openai:v0.6.0` And then run the following bash script (don't forget to replace with your...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eeds to convert the model to triton inference engine). When you run the H100 benchmark inside TensorRT-LLM docker container, you may experience a memory leaking issue ([issue link](https://github.com/triton-inference-se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
