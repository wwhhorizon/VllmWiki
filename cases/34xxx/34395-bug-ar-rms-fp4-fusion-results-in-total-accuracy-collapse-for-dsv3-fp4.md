# vllm-project/vllm#34395: [Bug]: AR+rms+fp4 fusion results in total accuracy collapse for DSV3-fp4

| 字段 | 值 |
| --- | --- |
| Issue | [#34395](https://github.com/vllm-project/vllm/issues/34395) |
| 状态 | closed |
| 标签 | bug;torch.compile;nvidia |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AR+rms+fp4 fusion results in total accuracy collapse for DSV3-fp4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` $ vllm serve nvidia/DeepSeek-V3.1-NVFP4 -tp=4 -cc.pass_config.fuse_allreduce_rms=True local-completions (pretrained=nvidia/DeepSeek-V3.1-NVFP4,base_url=http://0.0.0.0:8000/v1/completions,num_concurrent=50,max_retries=3), gen_kwargs: (None), limit: 100.0, num_fewshot: 5, batch_size: auto ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0|± | 0| | | |strict-match | 5|exact_match|↑ | 0|± | 0| ``` $ vllm serve nvidia/DeepSeek-V3.1-NVFP4 -tp=4 -cc.pass_config.fuse_allreduce_rms=False local-completions (pretrained=nvidia/DeepSeek-V3.1-NVFP4,base_url=http://0.0.0.0:8000/v1/completions,num_concurrent=50,max_retries=3), gen_kwargs: (None), limit: 100.0, num_fewshot: 5, batch_size: auto ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0.97|± |0.0171| | | |strict-match | 5|exact_match|↑ | 0.97|± |0.0171| ``` # also broken for v3.2 $ vllm serve nvidia/DeepSeek-V3.2-NVFP4 -tp=4 -...

## 现有链接修复摘要

#34899 Bump Flashinfer Version and Re-enable DeepSeek NVFP4 AR+Norm Fusion

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rms+fp4 fusion results in total accuracy collapse for DSV3-fp4 bug;torch.compile;nvidia ### Your current environment ### 🐛 Describe the bug ``` $ vllm serve nvidia/DeepSeek-V3.1-NVFP4 -tp=4 -cc.pass_config.fuse_allreduc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ribe the bug ``` $ vllm serve nvidia/DeepSeek-V3.1-NVFP4 -tp=4 -cc.pass_config.fuse_allreduce_rms=True local-completions (pretrained=nvidia/DeepSeek-V3.1-NVFP4,base_url=http://0.0.0.0:8000/v1/completions,num_concurrent=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: AR+rms+fp4 fusion results in total accuracy collapse for DSV3-fp4 bug;torch.compile;nvidia ### Your current environment ### 🐛 Describe the bug ``` $ vllm serve nvidia/DeepSeek-V3.1-NVFP4 -tp=4 -cc.pass_config.fus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0|± | 0| | | |strict-match | 5|exact_match|↑ | 0|± | 0| ``` $ vllm serve nvidia/DeepSeek-V3.1-NVFP4 -t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency #34899 Bump Flashinfer Version and Re-enable DeepSeek NVFP4 AR+Norm Fusion Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34899](https://github.com/vllm-project/vllm/pull/34899) | mentioned | 0.6 | Bump Flashinfer Version and Re-enable DeepSeek NVFP4 AR+Norm Fusion | 57) for fixing the Deepseek V3 accuracy issue with AR+rms+fp4 fusion (#34395) is included in flashinfer 0.6.4. This PR bumps flashinfer version and re-enables the fusion pass by d… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
