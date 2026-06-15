# vllm-project/vllm#13962: [Bug]: Download model many times when use VLLM_USE_MODELSCOPE and --tensor-parallel-size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#13962](https://github.com/vllm-project/vllm/issues/13962) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Download model many times when use VLLM_USE_MODELSCOPE and --tensor-parallel-size > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using VLLM_USE_MODELSCOPE and the tensor-parallel-size > 1, I found that vllm will download the model many times (eq to tensor-parallel-size) This makes start up slowly. And failed. the started command: ``` python3 -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5b --tensor-parallel-size 2 --dtype half ``` ``` # sometimes sha256 signature check failed: 2025-02-27T18:17:20.137937040+08:00 (VllmWorkerProcess pid=118) ERROR 02-27 02:17:20 multiproc_worker_utils.py:242] raise FileIntegrityError(msg) 2025-02-27T18:17:20.137940628+08:00 (VllmWorkerProcess pid=118) ERROR 02-27 02:17:20 multiproc_worker_utils.py:242] modelscope.hub.errors.FileIntegrityError: File /root/.cache/modelscope/hub/._____temp/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5b/model.safetensors integrity check failed, expected sha256 signature is 58858233513d76b8703e72eed6ce16807b523328188e13329257fb9594462945, actual is 2f3a36569365da73f53564947d17c5617a01976046095051663622d34d3539d6, the download may be incomplete, please try again # sometimes can not find some files 2025-02-27T18:17:34.673807661+08:00 ERROR 02-27 02:17:34 engin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Download model many times when use VLLM_USE_MODELSCOPE and --tensor-parallel-size > 1 bug ### Your current environment ### 🐛 Describe the bug When using VLLM_USE_MODELSCOPE and the tensor-parallel-size > 1, I fou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 8+08:00 ERROR 02-27 02:17:34 engine.py:389] copyfile(src, dst, follow_symlinks=follow_symlinks) 2025-02-27T18:17:34.674118892+08:00 ERROR 02-27 02:17:34 engine.py:389] File "/usr/lib/python3.12/shutil.py", line 260, in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: del deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5b --tensor-parallel-size 2 --dtype half ``` ``` # sometimes sha256 signature check failed: 2025-02-27T18:17:20.137937040+08:00 (VllmWorkerProcess pid=118) ERROR 02-27 02:17:20...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
