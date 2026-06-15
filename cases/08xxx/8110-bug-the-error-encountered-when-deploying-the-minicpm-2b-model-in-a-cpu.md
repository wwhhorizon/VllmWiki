# vllm-project/vllm#8110: [Bug]: The error encountered when deploying the MiniCPM-2B model in a CPU environment using the VLLM framework

| 字段 | 值 |
| --- | --- |
| Issue | [#8110](https://github.com/vllm-project/vllm/issues/8110) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The error encountered when deploying the MiniCPM-2B model in a CPU environment using the VLLM framework

### Issue 正文摘录

### Your current environment Support for OpenVINO on CPU-based VLLM environment Official documentation states that VLLM supports the MiniCPM-2B model ```text optimum-cli export openvino -m MiniCPM-2B --task text-generation-with-past --weight-format int4 ``` ### 🐛 Describe the bug root@2ae2daef803e:~# optimum-cli export openvino -m MiniCPM-2B --task text-generation-with-past --weight-format int4 MiniCPM-2B-int4 Framework not specified. Using pt to export the model. Traceback (most recent call last): File "/usr/local/bin/optimum-cli", line 8, in sys.exit(main()) File "/usr/local/lib/python3.10/dist-packages/optimum/commands/optimum_cli.py", line 208, in main service.run() File "/usr/local/lib/python3.10/dist-packages/optimum/commands/export/openvino.py", line 356, in run main_export( File "/usr/local/lib/python3.10/dist-packages/optimum/exporters/openvino/__main__.py", line 214, in main_export config = AutoConfig.from_pretrained( File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 975, in from_pretrained trust_remote_code = resolve_trust_remote_code( File "/usr/local/lib/python3.10/dist-packages/transformers/dynamic_module_utils.py", l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: The error encountered when deploying the MiniCPM-2B model in a CPU environment using the VLLM framework bug ### Your current environment Support for OpenVINO on CPU-based VLLM environment Official documentation s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rent environment Support for OpenVINO on CPU-based VLLM environment Official documentation states that VLLM supports the MiniCPM-2B model ```text optimum-cli export openvino -m MiniCPM-2B --task text-generation-with-pas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: openvino -m MiniCPM-2B --task text-generation-with-past --weight-format int4 ``` ### 🐛 Describe the bug root@2ae2daef803e:~# optimum-cli export openvino -m MiniCPM-2B --task text-generation-with-past --weight-format int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
