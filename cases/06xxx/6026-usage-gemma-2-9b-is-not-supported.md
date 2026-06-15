# vllm-project/vllm#6026: [Usage]: Gemma-2-9b is not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#6026](https://github.com/vllm-project/vllm/issues/6026) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Gemma-2-9b is not supported

### Issue 正文摘录

### Your current environment This is my vllm versions vllm 0.5.0.post1 vllm-flash-attn 2.5.9 vllm-nccl-cu11 2.18.1.0.4.0 ### How would you like to use vllm I want to run inference of a gemma-2-9b, which appears in the supported models list in the website. This is the code ``` from vllm import LLM, SamplingParams model_name = "google/gemma-2-9b" # You can change this to any other supported model llm = LLM(model=model_name, dtype=torch.float16, device="auto", tensor_parallel_size=2) ``` I'm getting the error: (VllmWorkerProcess pid=225845) ERROR 07-01 10:50:45 multiproc_worker_utils.py:226] ValueError: Model architectures ['Gemma2ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LlavaForConditionalGeneration', 'LlavaNextForC...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Gemma-2-9b is not supported usage ### Your current environment This is my vllm versions vllm 0.5.0.post1 vllm-flash-attn 2.5.9 vllm-nccl-cu11 2.18.1.0.4.0
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 2-9b is not supported usage ### Your current environment This is my vllm versions vllm 0.5.0.post1 vllm-flash-attn 2.5.9 vllm-nccl-cu11 2.18.1.0.4.0 ### How would you like to use vllm I want to run inference of a gemma-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: can change this to any other supported model llm = LLM(model=model_name, dtype=torch.float16, device="auto", tensor_parallel_size=2) ``` I'm getting the error: (VllmWorkerProcess pid=225845) ERROR 07-01 10:50:45 multipr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 5) ERROR 07-01 10:50:45 multiproc_worker_utils.py:226] ValueError: Model architectures ['Gemma2ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM'...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: Gemma-2-9b is not supported usage ### Your current environment This is my vllm versions vllm 0.5.0.post1 vllm-flash-attn 2.5.9 vllm-nccl-cu11 2.18.1.0.4.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
