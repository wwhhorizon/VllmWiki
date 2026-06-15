# vllm-project/vllm#23988: Accuracy Drop with OpenGVLab/InternVL3-14B when using vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#23988](https://github.com/vllm-project/vllm/issues/23988) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Accuracy Drop with OpenGVLab/InternVL3-14B when using vLLM

### Issue 正文摘录

I have observed a significant drop in accuracy when running the OpenGVLab/InternVL3-14B model on vLLM compared to LMDeploy. The evaluation was performed on [mention your evaluation dataset/task]. **Reproducible Steps:** 1. **LMDeploy:** ```bash lmdeploy serve api_server OpenGVLab/InternVL3-14B --chat-template internvl2_5 --cache-max-entry-count 0.8 --server-port 7000 --tp 1 --session-len 13000 --max-batch-size 1 --eager-mode --dtype float16 ``` 2. **vLLM:** ```bash python -m vllm.entrypoints.openai.api_server --model OpenGVLab/InternVL3-14B --trust-remote-code --max-model-len 13000 --tensor-parallel-size 1 --gpu-memory-utilization 0.75 --dtype float16 --port 7000 --enforce-eager --max-num-seqs 8 --swap-space 4 ``` **Expected Behavior:** The accuracy on vLLM should be comparable to or the same as LMDeploy, assuming both are running the same model and configuration. **Actual Behavior:** The accuracy on vLLM is lower. - **LMDeploy Accuracy:** 95% - **vLLM Accuracy:** 75% **Environment:** - **vLLM Version:** 0.9.2 - **LMDeploy Version:** 0.9.2 - **PyTorch Version:** 2.7.0 (vLLM) and 2.7.1 (LMDeploy) - **CUDA Version:** 12.2 - **GPU:** NVIDIA A100 80GB - **Driver Version:** 535.230.02...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ation was performed on [mention your evaluation dataset/task]. **Reproducible Steps:** 1. **LMDeploy:** ```bash lmdeploy serve api_server OpenGVLab/InternVL3-14B --chat-template internvl2_5 --cache-max-entry-count 0.8 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Accuracy Drop with OpenGVLab/InternVL3-14B when using vLLM I have observed a significant drop in accuracy when running the OpenGVLab/InternVL3-14B model on vLLM compared to LMDeploy. The evaluation was performed on [men...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Accuracy Drop with OpenGVLab/InternVL3-14B when using vLLM I have observed a significant drop in accuracy when running the OpenGVLab/InternVL3-14B model on vLLM compared to LMDeploy. The evaluation was performed on [ment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: r-port 7000 --tp 1 --session-len 13000 --max-batch-size 1 --eager-mode --dtype float16 ``` 2. **vLLM:** ```bash python -m vllm.entrypoints.openai.api_server --model OpenGVLab/InternVL3-14B --trust-remote-code --max-mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: * 0.9.2 - **PyTorch Version:** 2.7.0 (vLLM) and 2.7.1 (LMDeploy) - **CUDA Version:** 12.2 - **GPU:** NVIDIA A100 80GB - **Driver Version:** 535.230.02 I have confirmed that both frameworks are loading the same model. co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
