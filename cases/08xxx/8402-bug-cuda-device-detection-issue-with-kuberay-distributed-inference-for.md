# vllm-project/vllm#8402: [Bug]: CUDA device detection issue with KubeRay distributed inference for quantized models 

| 字段 | 值 |
| --- | --- |
| Issue | [#8402](https://github.com/vllm-project/vllm/issues/8402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA device detection issue with KubeRay distributed inference for quantized models 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 2 nodes with 1 GPU each in a Kubernetes environment. Each of those GPUs is too small to load the model (hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4) by itself, hence what I want is to run 2 replicas of vllm over ray to split the weights (PIPELINE_PARALLEL_SIZE config) between the two. I was able to do that, using this [guide](https://docs.vllm.ai/en/latest/serving/distributed_serving.html). This is the command I used to launch quantized llama3.1:70b - `python3 -m vllm.entrypoints.openai.api_server --port 8080 --served-model-name llama3.1:70b --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --max-model-len 4096 --tokenizer hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --dtype half -q marlin --tensor-parallel-size 1 --pipeline-parallel-size 2`. It successfully runs the model over 3 pods (ray head + 2 ray workers), where each worker has access to its own GPU (46GB) However, I'm unable to do the same thing with Kuberay, launching a model via RayService. Whenever I try to launch a **quantized** model I get the following error: `RuntimeError: CUDA_VISIBLE_DEVICES is se...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Bug]: CUDA device detection issue with KubeRay distributed inference for quantized models bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 2 nodes with 1 GPU each in a K...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA device detection issue with KubeRay distributed inference for quantized models bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 2 nodes with 1 GPU each in a
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: device detection issue with KubeRay distributed inference for quantized models bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 2 nodes with 1 GPU each in a Kubernetes e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
