# vllm-project/vllm#11568: [Performance]: The performance of bge-rerank model on vllm and huggingface is inconsistent

| 字段 | 值 |
| --- | --- |
| Issue | [#11568](https://github.com/vllm-project/vllm/issues/11568) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: The performance of bge-rerank model on vllm and huggingface is inconsistent

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance The script loaded using vllm is: ``` from vllm import LLM model_path = "/data/reranker/bge-reranker-large" # Create an LLM. # You should pass task="score" for cross-encoder models model = LLM( model=model_path, task="score", enforce_eager=True, dtype="float32" ) ``` huggingface scripts mainly use default parameters for，float32 ``` CrossEncoder( model, max_length=512, device=device ) ``` After running 200 sets of data, in which 100 paragraphs were rearranged, 19 sets were found to be in inconsistent order after rearrangement I also looked up some information online and there is the following information： https://zhuanlan.zhihu.com/p/658780653 I do not know whether the parameter of my vllm is wrong, or what causes it? ### Your current environment (if you think it is necessary) Current environment linux: ubuntu 18 NVIDIA-SMI 525.105.17 Driver Version: 525.105.17 CUDA Version: 12.0 Tesla T4 vllm==0.6.6 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: iscussion on performance The script loaded using vllm is: ``` from vllm import LLM model_path = "/data/reranker/bge-reranker-large" # Create an LLM. # You should pass task="score" for cross-encoder models model = LLM( m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ou think it is necessary) Current environment linux: ubuntu 18 NVIDIA-SMI 525.105.17 Driver Version: 525.105.17 CUDA Version: 12.0 Tesla T4 vllm==0.6.6 ### Before submitting a new issue... - [X] Make sure you already se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: The performance of bge-rerank model on vllm and huggingface is inconsistent performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discus...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: LLM( model=model_path, task="score", enforce_eager=True, dtype="float32" ) ``` huggingface scripts mainly use default parameters for，float32 ``` CrossEncoder( model, max_length=512, device=device ) ``` After running 200...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance The script loaded using vllm is: ``` from vllm import LLM model_path = "/data/reranker/b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
