# vllm-project/vllm#22620: [Bug]: Cant classify with ModernBERT

| 字段 | 值 |
| --- | --- |
| Issue | [#22620](https://github.com/vllm-project/vllm/issues/22620) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Cant classify with ModernBERT

### Issue 正文摘录

### Your current environment v0.10.0 ### 🐛 Describe the bug Trying to run a classification model with ModernBERT architecture (ModernBertForSequenceClassification). It fails with both pooling 'cls' and 'mean'. Model tested: `cirimus/modernbert-base-go-emotions` ```bash vllm serve cirimus/modernbert-base-go-emotions --task classify ``` Error: ``` Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 9.88it/s] Process SpawnProcess-1: Traceback (most recent call last): File "/opt/anaconda/envs/transformers/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/opt/anaconda/envs/transformers/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/user/codes/website/legal-search/venv/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 458, in run_mp_engine raise e from None File "/home/user/codes/website/legal-search/venv/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 444, in run_mp_engine engine = MQLLMEngine.from_vllm_config( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/user/codes/website/legal-search/venv/lib/python3.12/site-pack...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ronment v0.10.0 ### 🐛 Describe the bug Trying to run a classification model with ModernBERT architecture (ModernBertForSequenceClassification). It fails with both pooling 'cls' and 'mean'. Model tested: `cirimus/modernb...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ification). It fails with both pooling 'cls' and 'mean'. Model tested: `cirimus/modernbert-base-go-emotions` ```bash vllm serve cirimus/modernbert-base-go-emotions --task classify ``` Error: ``` Loading safetensors chec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 🐛 Describe the bug Trying to run a classification model with ModernBERT architecture (ModernBertForSequenceClassification). It fails with both pooling 'cls' and 'mean'. Model tested: `cirimus/modernbert-base-go-emotions...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: uenceClassification). It fails with both pooling 'cls' and 'mean'. Model tested: `cirimus/modernbert-base-go-emotions` ```bash vllm serve cirimus/modernbert-base-go-emotions --task classify ``` Error: ``` Loading safete...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
