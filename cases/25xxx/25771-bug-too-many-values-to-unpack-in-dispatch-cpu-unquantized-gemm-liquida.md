# vllm-project/vllm#25771: [Bug]: Too many values to unpack in dispatch_cpu_unquantized_gemm [LiquidAi/LMF2]

| 字段 | 值 |
| --- | --- |
| Issue | [#25771](https://github.com/vllm-project/vllm/issues/25771) |
| 状态 | open |
| 标签 | bug;unstale;cpu |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Too many values to unpack in dispatch_cpu_unquantized_gemm [LiquidAi/LMF2]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have installed VLLM by following official documentation on how to install it with python on a CPU only machine. I also tried directly to serve the model with the CPU docker build. Here is and example of testing code. (vllm cpu) ```python from vllm import LLM def main(): llm = LLM(model="LiquidAI/LFM2-2.6B", dtype="float32") prompt = "Bonjour, comment ça va ?" for output in llm.generate(prompt): print(output.text) if __name__ == "__main__": main() ``` Here is the output. ```python python test.py [W926 18:06:18.057966816 OperatorEntry.cpp:218] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Tensor registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: AutocastCPU previous kernel: registered at /pytorch/aten/src/ATen/autocast_mode.cpp:327 new kernel: registered at /opt/workspace/ipex-cpu-dev/csrc/cpu/autocast/autocast_mode.cpp:112 (function operator()) I...

## 现有链接修复摘要

#35059 feat(cpu): add CPU support for Mamba ShortConv and fix GEMM dispatch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: tale;cpu ### Your current environment ### 🐛 Describe the bug I have installed VLLM by following official documentation on how to install it with python on a CPU only machine. I also tried directly to serve the model wit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Too many values to unpack in dispatch_cpu_unquantized_gemm [LiquidAi/LMF2] bug;unstale;cpu ### Your current environment ### 🐛 Describe the bug I have installed VLLM by following official documentation on how to i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: values to unpack in dispatch_cpu_unquantized_gemm [LiquidAi/LMF2] bug;unstale;cpu ### Your current environment ### 🐛 Describe the bug I have installed VLLM by following official documentation on how to install it with p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Too many values to unpack in dispatch_cpu_unquantized_gemm [LiquidAi/LMF2] bug;unstale;cpu ### Your current environment ### 🐛 Describe the bug I have installed VLLM by following official documentation on how to i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: sor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Tensor registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: AutocastCPU previous kernel: registered at /pytorch/a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35059](https://github.com/vllm-project/vllm/pull/35059) | closes_keyword | 0.95 | feat(cpu): add CPU support for Mamba ShortConv and fix GEMM dispatch | Fixes: #25771 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
