# vllm-project/vllm#17689: [Bug]: gemma3 shows degraded accuracy in vLLM v0.8.4

| 字段 | 值 |
| --- | --- |
| Issue | [#17689](https://github.com/vllm-project/vllm/issues/17689) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma3 shows degraded accuracy in vLLM v0.8.4

### Issue 正文摘录

### Your current environment - vLLM version: v0.8.4 - docker image: nvcr.io/nvidia/pytorch/23.10-py3 - install script ``` pip install -r ./requirements/build.txt pip install -r ./requirements/common.txt pip install -r ./requirements/cuda.txt pip install flash_attn==2.7.4.post1 export VLLM_COMMIT=dc1b4a6f1300003ae27f033afbdff5e2683721ce export VLLM_PRECOMPILED_WHEEL_LOCATION=https://wheels.vllm.ai/${VLLM_COMMIT}/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl pip install -e . pip install -U pynvml ``` ### 🐛 Describe the bug I'm testing open-source models using vLLM v0.8.4 and [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness). However, this version shows degraded accuracy when deploying the Gemma 3 series. There were no issues when testing the Qwen 2.5 model. I'm comparing results from vLLM against those from Hugging Face. ## Qwen2.5-72B-Instruct ### vLLM result | Tasks |Version|Filter|n-shot| Metric | |Value | |Stderr| |--------------|------:|------|-----:|----------|---|-----:|---|-----:| |hellaswag | 1|none | 0|acc |↑ |0.7042|± |0.0046| | | |none | 0|acc_norm |↑ |0.8741|± |0.0033| |lambada_openai| 1|none | 0|acc |↑ |0.7613|± |0.0059| | | |none | 0|perple...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: degraded accuracy in vLLM v0.8.4 bug ### Your current environment - vLLM version: v0.8.4 - docker image: nvcr.io/nvidia/pytorch/23.10-py3 - install script ``` pip install -r ./requirements/build.txt pip install -r ./req...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gemma3 shows degraded accuracy in vLLM v0.8.4 bug ### Your current environment - vLLM version: v0.8.4 - docker image: nvcr.io/nvidia/pytorch/23.10-py3 - install script ``` pip install -r ./requirements/build.txt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: gemma3 shows degraded accuracy in vLLM v0.8.4 bug ### Your current environment - vLLM version: v0.8.4 - docker image: nvcr.io/nvidia/pytorch/23.10-py3 - install script ``` pip install -r ./requirements/build.txt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t pip install -r ./requirements/common.txt pip install -r ./requirements/cuda.txt pip install flash_attn==2.7.4.post1 export VLLM_COMMIT=dc1b4a6f1300003ae27f033afbdff5e2683721ce export VLLM_PRECOMPILED_WHEEL_LOCATION=ht...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d_parallel;hardware_porting;model_support;quantization cuda;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
