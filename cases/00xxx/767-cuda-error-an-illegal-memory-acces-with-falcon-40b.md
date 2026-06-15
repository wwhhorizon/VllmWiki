# vllm-project/vllm#767: CUDA error: an illegal memory acces with Falcon 40B

| 字段 | 值 |
| --- | --- |
| Issue | [#767](https://github.com/vllm-project/vllm/issues/767) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA error: an illegal memory acces with Falcon 40B

### Issue 正文摘录

Hi, I am testing different models with vllm. I see ```CUDA error: an illegal memory access``` when I use falcon 40 b. The code I use is ``` llm = LLM(model=ckpt_dir,tensor_parallel_size=4,trust_remote_code=True,gpu_memory_utilization=0.8) sampling_params = SamplingParams(temperature=0, top_p=1.0, max_tokens=300) results = llm.generate(prompts, sampling_params) ``` I am using an A100 with 4 GPUs. Please let me know if you have any questions

## 现有链接修复摘要

#992 fix: CUDA error when inferencing with Falcon-40B base model

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: CUDA error: an illegal memory acces with Falcon 40B bug Hi, I am testing different models with vllm. I see ```CUDA error: an illegal memory access``` when I use falcon 40 b. The code I use is ``` llm = LLM(model=ckpt_d
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l_support;sampling_logits cuda;sampling #992 fix: CUDA error when inferencing with Falcon-40B base model Hi,
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: : an illegal memory acces with Falcon 40B bug Hi, I am testing different models with vllm. I see ```CUDA error: an illegal memory access``` when I use falcon 40 b. The code I use is ``` llm = LLM(model=ckpt_dir,tensor_p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: CUDA error: an illegal memory acces with Falcon 40B bug Hi, I am testing different models with vllm. I see ```CUDA error: an illegal memory access``` when I use falcon 40 b. The code I use is ``` llm = LLM(model=ckpt_di...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#992](https://github.com/vllm-project/vllm/pull/992) | closes_keyword | 0.95 | fix: CUDA error when inferencing with Falcon-40B base model | resolves #767. As described on https://github.com/vllm-project/vllm/issues/767#issuecomment-1699136748, referencing `model_type` instance variable results in wrongly determining mo |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
