# vllm-project/vllm#39433: RFC: Add logit_scale to PoolerConfig for Affine Score Calibration (Platt Scaling)

| 字段 | 值 |
| --- | --- |
| Issue | [#39433](https://github.com/vllm-project/vllm/issues/39433) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RFC: Add logit_scale to PoolerConfig for Affine Score Calibration (Platt Scaling)

### Issue 正文摘录

## Motivation vLLM's `PoolerConfig` already supports `logit_bias` for classification models, enabling a bias offset on raw logits before activation. However, there is no corresponding **scale** parameter, which means vLLM cannot express the standard affine calibration transform: ``` calibrated_score = activation(scale * (logit - bias)) ``` This transform is known as **Platt scaling** (Platt, 1999) — the most widely-used method for calibrating classifier outputs into well-calibrated probabilities. It fits two parameters (A and B) such that: ``` P(y=1|x) = sigmoid(A * f(x) + B) ``` where `f(x)` is the raw model output. This is equivalent to `sigmoid(A * (f(x) - (-B/A)))`, i.e. scale and bias. **Reference:** John Platt. "Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods." Advances in Large Margin Classifiers, 1999. Platt scaling is not limited to SVMs — it is routinely applied to neural network classifiers, cross-encoders, and reranking models to map raw logits into interpretable probability scores. Related techniques include: - **Temperature scaling** (Guo et al., 2017) — a special case where only scale is learned (`bias=0`) - **Sent...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: techniques include: - **Temperature scaling** (Guo et al., 2017) — a special case where only scale is learned (`bias=0`) - **SentenceTransformers cross-encoder activation functions** — vLLM already supports loading thes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: dation set without retraining the model. With `logit_scale`, models can ship calibration parameters in their config and produce calibrated scores out of the box. ### 2. Temperature scaling for confidence calibration Mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: RFC: Add logit_scale to PoolerConfig for Affine Score Calibration (Platt Scaling) ## Motivation vLLM's `PoolerConfig` already supports `logit_bias` for classification models, enabling a bias offset on raw logits before...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: RFC: Add logit_scale to PoolerConfig for Affine Score Calibration (Platt Scaling) ## Motivation vLLM's `PoolerConfig` already supports `logit_bias` for classification models, enabling a bias offset on raw logits before...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
