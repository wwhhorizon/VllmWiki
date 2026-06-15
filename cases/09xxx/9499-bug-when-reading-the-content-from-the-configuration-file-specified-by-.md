# vllm-project/vllm#9499: [Bug]: When reading the content from the configuration file specified by the --config parameter, the parameter type was not considered.

| 字段 | 值 |
| --- | --- |
| Issue | [#9499](https://github.com/vllm-project/vllm/issues/9499) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When reading the content from the configuration file specified by the --config parameter, the parameter type was not considered.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The code in the method '_load_config_file' of vllm/vllm/utils.py which reads the config file from the parameter --config has a bug. ```python # only expecting a flat dictionary of atomic types processed_args: List[str] = [] config: Dict[str, Union[int, str]] = {} try: with open(file_path, 'r') as config_file: config = yaml.safe_load(config_file) except Exception as ex: logger.error( "Unable to read the config file at %s. \ Make sure path is correct", file_path) raise ex for key, value in config.items(): processed_args.append('--' + key) processed_args.append(str(value)) return processed_args ``` The code here simply spans the key-value pairs in the config file. So, if I want to store a 'store_true' parameter like '--trust-remote-code', I cannot put it in the config file. For example, I had test 'trust-remote-code:', 'trust-remote-code: ""', 'trust-remote-code: yes', 'trust-remote-code: true'. When the key-value pairs were spanned, the cli parameters will be like 'vllm server model_name --trust-remote-code true'. Then an error be like saying 'there is no parameter named "true"' will happened. ##...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When reading the content from the configuration file specified by the --config parameter, the parameter type was not considered. bug;help wanted;good first issue ### Your current environment ### Model Input Dumps...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: When reading the content from the configuration file specified by the --config parameter, the parameter type was not considered. bug;help wanted;good first issue ### Your current environment ### Model Input Dumps...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: st-remote-code', I cannot put it in the config file. For example, I had test 'trust-remote-code:', 'trust-remote-code: ""', 'trust-remote-code: yes', 'trust-remote-code: true'. When the key-value pairs were spanned, the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
