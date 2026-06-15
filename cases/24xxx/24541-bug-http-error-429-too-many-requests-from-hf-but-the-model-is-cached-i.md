# vllm-project/vllm#24541: [Bug]: Http error 429 (too many requests) from HF, but the model is cached in HF_HOME

| 字段 | 值 |
| --- | --- |
| Issue | [#24541](https://github.com/vllm-project/vllm/issues/24541) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Http error 429 (too many requests) from HF, but the model is cached in HF_HOME

### Issue 正文摘录

### Your current environment vllm 0.10.0 ### 🐛 Describe the bug I've hit this exception while working with trinity/verl. But I've got the Qwen model well cached in the `$HF_HOME` directory. Does vllm hit internet / HF api even if the model is available in the local cache? ``` :job_id:06000000 :actor_name:vLLMRolloutModel `torch_dtype` is deprecated! Use `dtype` instead! Process EngineCore_0: Traceback (most recent call last): File "/tmp/ray/session_2025-09-09_21-51-38_617712_92779/runtime_resources/working_dir_files/_ray_pkg_ba5689fe78f8c669/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_http.py", line 409, in hf_raise_for_status response.raise_for_status() File "/tmp/ray/session_2025-09-09_21-51-38_617712_92779/runtime_resources/working_dir_files/_ray_pkg_ba5689fe78f8c669/.venv/lib/python3.12/site-packages/requests/models.py", line 1026, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 429 Client Error: Too Many Requests for url: https://huggingface.co/api/models/Qwen/Qwen2.5-1.5B-Instruct The above exception was the direct cause of the following exception: Traceback (most recent call last): File "/usr/lib/python3.12/mul...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Http error 429 (too many requests) from HF, but the model is cached in HF_HOME bug ### Your current environment vllm 0.10.0 ### 🐛 Describe the bug I've hit this exception while working with trinity/verl. But I've...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: local cache? ``` :job_id:06000000 :actor_name:vLLMRolloutModel `torch_dtype` is deprecated! Use `dtype` instead! Process EngineCore_0: Traceback (most recent call last): File "/tmp/ray/session_2025-09-09_21-51-38_617712...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nload_weights_from_hf file_list = fs.ls(model_name_or_path, detail=False, revision=revision) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/tmp/ray/session_2025-09-09_21-51-38_617712_92779/runtime_res...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Http error 429 (too many requests) from HF, but the model is cached in HF_HOME bug ### Your current environment vllm 0.10.0 ### 🐛 Describe the bug I've hit this exception while working with trinity/verl. But I've...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
