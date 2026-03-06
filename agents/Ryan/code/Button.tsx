import React from 'react';
import { Pressable, Text, StyleSheet, ViewStyle, TextStyle } from 'react-native';
import tokens from '../tokens.json';

type ButtonProps = {
  title: string;
  onPress?: () => void;
  disabled?: boolean;
  style?: ViewStyle;
  textStyle?: TextStyle;
  testID?: string;
};

const Button: React.FC<ButtonProps> = ({ title, onPress, disabled = false, style, textStyle, testID }) => {
  return (
    <Pressable
      testID={testID}
      onPress={onPress}
      disabled={disabled}
      style={({ pressed }) => [styles.button, pressed && styles.pressed, disabled && styles.disabled, style]}
      accessibilityRole="button"
      accessibilityState={{ disabled }}
    >
      <Text style={[styles.text, textStyle]}>{title}</Text>
    </Pressable>
  );
};

const styles = StyleSheet.create({
  button: {
    backgroundColor: tokens.colors.primary,
    paddingVertical: tokens.spacing.sm,
    paddingHorizontal: tokens.spacing.md,
    borderRadius: tokens.radii.md,
    alignItems: 'center',
    justifyContent: 'center',
  },
  pressed: {
    opacity: 0.85,
  },
  disabled: {
    backgroundColor: tokens.colors.gray300,
  },
  text: {
    color: tokens.colors.onPrimary,
    fontSize: tokens.typography.button.fontSize,
    fontWeight: tokens.typography.button.fontWeight as any,
  },
});

export default Button;
