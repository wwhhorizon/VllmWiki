# vllm-project/vllm#244: [Roadmap] vLLM Development Roadmap: H2 2023

| 字段 | 值 |
| --- | --- |
| Issue | [#244](https://github.com/vllm-project/vllm/issues/244) |
| 状态 | closed |
| 标签 |  |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;quantization;sampling;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap] vLLM Development Roadmap: H2 2023

### Issue 正文摘录

We summarize the issues we received and our planned features in this issue. This issue will keep being updated. Latest issue tracked: #677 ## Software Quality - [x] Code formater #57 - [x] Tests for model correctness #101 - [x] Tests for samplers #108 - [ ] Pypi CD #97 - [x] CI ## Installation - [x] CUDA version #129 - [x] Pre-built CUDA Wheels #139 #695 - [x] Support ROCM #621 - [x] Windows/WSL installation #179 #192 - [x] H100 #199 #407 - [x] Support CUDA 12 #385 - [x] Dockerfile #390 - [ ] All other issues with `Installation` label ## Documentation - [x] Documentation CD - [x] Documentation on LLMEngine and AsyncLLMEngine - [x] Documentation on user interfaces and the APIs #361 #395 - [x] Documentation on distributed execution #206 #228 #243 #250 #581 - [x] More detailed guide on adding a new model (possibly simplification in code). Especially how to modify the `forward` function. #242 - [ ] Include latency benchmark results. - [ ] On memory usage. #241 #550 - [x] How to specify which GPU to use #691 #571 ## New Models Decoder-only models - [x] BLOOM #61 - [x] Falcon #195 #197 #356 - [x] GPT-J #198 - [x] MPT #218 #332 - [x] LongChat #358 - [x] Baichuan-7B #303 #400 #428 - [x] B...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: orrectness #101 - [x] Tests for samplers #108 - [ ] Pypi CD #97 - [x] CI ## Installation - [x] CUDA version #129 - [x] Pre-built CUDA Wheels #139 #695 - [x] Support ROCM #621 - [x] Windows/WSL installation #179 #192 - [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ts for samplers #108 - [ ] Pypi CD #97 - [x] CI ## Installation - [x] CUDA version #129 - [x] Pre-built CUDA Wheels #139 #695 - [x] Support ROCM #621 - [x] Windows/WSL installation #179 #192 - [x] H100 #199 #407 - [x] S...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 434 #668 - [ ] BART #187 - [x] GLM #231 #247 Other techniques: - [x] Quantized models: see Kernels/Quantized PagedAttention - [x] LoRA: #182 - [ ] Multi-modal models: #307 ## Frontend Features vLLM demo frontends: - [x]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g updated. Latest issue tracked: #677 ## Software Quality - [x] Code formater #57 - [x] Tests for model correctness #101 - [x] Tests for samplers #108 - [ ] Pypi CD #97 - [x] CI ## Installation - [x] CUDA version #129 -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: r planned features in this issue. This issue will keep being updated. Latest issue tracked: #677 ## Software Quality - [x] Code formater #57 - [x] Tests for model correctness #101 - [x] Tests for samplers #108 - [ ] Pyp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
