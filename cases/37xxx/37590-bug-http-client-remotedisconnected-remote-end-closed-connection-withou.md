# vllm-project/vllm#37590: [Bug]: http.client.RemoteDisconnected: Remote end closed connection without response

| 字段 | 值 |
| --- | --- |
| Issue | [#37590](https://github.com/vllm-project/vllm/issues/37590) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;moe;sampling |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: http.client.RemoteDisconnected: Remote end closed connection without response

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Sometimes when prompts contain large tables, server tends to silently disconnect from the client. No any logs on server side. If prompts in script truncated to some degree, vllm can respond correctly. Exception on Client Side: ```bash Traceback (most recent call last): File "/opt/AI/.venv/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen response = self._make_request( ^^^^^^^^^^^^^^^^^^^ File "/opt/AI/.venv/lib/python3.12/site-packages/urllib3/connectionpool.py", line 534, in _make_request response = conn.getresponse() ^^^^^^^^^^^^^^^^^^ File "/opt/AI/.venv/lib/python3.12/site-packages/urllib3/connection.py", line 571, in getresponse httplib_response = super().getresponse() ^^^^^^^^^^^^^^^^^^^^^ File "/home/user/.local/share/uv/python/cpython-3.12.11-linux-x86_64-gnu/lib/python3.12/http/client.py", line 1430, in getresponse response.begin() File "/home/user/.local/share/uv/python/cpython-3.12.11-linux-x86_64-gnu/lib/python3.12/http/client.py", line 331, in begin version, status, reason = self._read_status() ^^^^^^^^^^^^^^^^^^^ File "/home/user/.local/share/uv/python/cpython-3.12.11-linux-x86_64-gnu/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -linux-x86_64-gnu/lib/python3.12/http/client.py", line 331, in begin version, status, reason = self._read_status() ^^^^^^^^^^^^^^^^^^^ File "/home/user/.local/share/uv/python/cpython-3.12.11-linux-x86_64-gnu/lib/python3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: KEN = 'sk-xxxx' def get_content_large_table(): """text from https://qwen.ai/blog?id=qwen3.5 """ return """ We are delighted to announce the official release of Qwen3.5, introducing the open-weight of the first model in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: chieve significantly greater productivity. Built on an innovative hybrid architecture that fuses linear attention (via Gated Delta Networks) with a sparse mixture-of-experts, the model attains remarkable inference effic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: wen3.5-397B-A17B demonstrates outstanding results across a full range of benchmark evaluations, including reasoning, coding, agent capabilities, and multimodal understanding, empowering developers and enterprises to ach...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ses linear attention (via Gated Delta Networks) with a sparse mixture-of-experts, the model attains remarkable inference efficiency: although it comprises 397 billion total parameters, just 17 billion are activated per...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
