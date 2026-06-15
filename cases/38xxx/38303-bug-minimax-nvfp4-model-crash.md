# vllm-project/vllm#38303: [Bug]: minimax nvfp4 model crash

| 字段 | 值 |
| --- | --- |
| Issue | [#38303](https://github.com/vllm-project/vllm/issues/38303) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: minimax nvfp4 model crash

### Issue 正文摘录

### Your current environment `vllm/vllm-openai:v0.18.0` ### 🐛 Describe the bug hi @kedarpotdar-nv probably should be simple fix to have model loader load the scales too ## reprod ``` vllm serve $MODEL --host 0.0.0.0 --port $PORT \ --tensor-parallel-size=$TP \ --gpu-memory-utilization 0.90 \ --max-model-len $MAX_MODEL_LEN \ --max-num-seqs $CONC \ --no-enable-prefix-caching \ --compilation_config.pass_config.fuse_allreduce_rms true \ --trust-remote-code ``` ## Error log ``` (Worker_TP3_EP3 pid=2222203) ERROR 03-27 01:32:45 [multiproc_executor.py:852] return original_load_weights(self, weights, *args, **kwargs) (Worker_TP3_EP3 pid=2222203) ERROR 03-27 01:32:45 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP3_EP3 pid=2222203) ERROR 03-27 01:32:45 [multiproc_executor.py:852] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 348, in load_weights (Worker_TP3_EP3 pid=2222203) ERROR 03-27 01:32:45 [multiproc_executor.py:852] autoloaded_weights = set(self._load_module("", self.module, weights)) (Worker_TP3_EP3 pid=2222203) ERROR 03-27 01:32:45 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: minimax nvfp4 model crash bug ### Your current environment `vllm/vllm-openai:v0.18.0` ### 🐛 Describe the bug hi @kedarpotdar-nv probably should be simple fix to have model loader load the scales too ## reprod ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: minimax nvfp4 model crash bug ### Your current environment `vllm/vllm-openai:v0.18.0` ### 🐛 Describe the bug hi @kedarpotdar-nv probably should be simple fix to have model loader load the scales too ## reprod ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
